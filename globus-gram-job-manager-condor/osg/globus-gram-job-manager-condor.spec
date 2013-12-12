%if "%{?rhel}" == "5"
%global docdiroption "with-docdir"
%else
%global docdiroption "docdir"
%endif

%{!?perl_vendorlib: %global perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)}

Name:		globus-gram-job-manager-condor
%global _name %(tr - _ <<< %{name})
Version:	1.0
Release:	13.4%{?dist}
Summary:	Globus Toolkit - Condor Job Manager

Group:		Applications/Internet
License:	ASL 2.0
URL:		http://www.globus.org/
Source:		http://www.globus.org/ftppub/gt5/5.2/5.2.0/packages/src/%{_name}-%{version}.tar.gz
Source1:        condor_accounting_groups.pm
Source2:        condor.rvf

# OSG Patches
Patch0:         job_status.patch
Patch1:         gratia.patch
Patch2:         nfslite.patch
Patch3:         groupacct.patch
Patch4:         managedfork.patch
Patch5:         conf_location.patch
Patch6:         669-xcount.patch
Patch7:         717-max-walltime.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Obsoletes:      globus-gram-job-manager-setup-condor < 4.5
Requires:	globus-gram-job-manager-scripts >= 3.4
Requires:	globus-gass-cache-program >= 2
Requires:	globus-common-progs >= 2
Requires:	globus-gram-job-manager >= 10.59
Requires:	globus-gatekeeper >= 7.3
Requires:       condor
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires(post): globus-gram-job-manager-scripts >= 4
Requires(preun): globus-gram-job-manager-scripts >= 4
Provides:       globus-gram-job-manager-setup
BuildRequires:	grid-packaging-tools >= 3.4
BuildRequires:	globus-core >= 8
BuildRequires:	doxygen
BuildRequires:	graphviz
%if "%{?rhel}" == "5"
BuildRequires:	graphviz-gd
%endif
BuildRequires:	ghostscript
%if %{?fedora}%{!?fedora:0} >= 9 || %{?rhel}%{!?rhel:0} >= 6
BuildRequires:	tex(latex)
%else
BuildRequires:	tetex-latex
%endif

%description
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name} package contains:
Condor Job Manager 

%prep
%setup -q -n %{_name}-%{version}

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0

%build
# Remove files that should be replaced during bootstrap
rm -f doxygen/Doxyfile*
rm -f doxygen/Makefile.am
rm -f pkgdata/Makefile.am
rm -f globus_automake*
rm -rf autom4te.cache

%{_datadir}/globus/globus-bootstrap.sh

export CONDOR_RM=/usr/bin/condor_rm
export CONDOR_SUBMIT=/usr/bin/condor_submit
%configure --%{docdiroption}=%{_docdir}/%{name}-%{version}

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# Remove jobmanager-condor from install dir so that it can be
# added/removed by post scripts
rm $RPM_BUILD_ROOT/etc/grid-services/jobmanager-condor

GLOBUSPACKAGEDIR=$RPM_BUILD_ROOT%{_datadir}/globus/packages

sed -i s!$RPM_BUILD_ROOT!! $GLOBUSPACKAGEDIR/%{_name}/noflavor_data.filelist

# Generate package filelists
cat $GLOBUSPACKAGEDIR/%{_name}/noflavor_data.filelist \
    $GLOBUSPACKAGEDIR/%{_name}/noflavor_doc.filelist \
    $GLOBUSPACKAGEDIR/%{_name}/noflavor_rtl.filelist \
  | sed s!^!%{_prefix}! \
  | sed s!^%{_prefix}/etc!/etc! > package.filelist

cat package.filelist

## OSG-specific additions
cat >> $RPM_BUILD_ROOT%{_sysconfdir}/globus/globus-condor.conf << EOF

# Enable Condor file transfer mode by default on the OSG
isNFSLite=1

EOF

# Install the group accounting patch
mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}/Globus/GRAM/JobManager/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{perl_vendorlib}/Globus/GRAM/JobManager/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/osg
touch $RPM_BUILD_ROOT%{_sysconfdir}/osg/uid_table.txt
touch $RPM_BUILD_ROOT%{_sysconfdir}/osg/extattr_table.txt

# Install the RVF file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/globus/gram/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/globus/gram/condor.rvf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ $1 -eq 1 ]; then
    globus-gatekeeper-admin -e jobmanager-condor > /dev/null 2>&1 || :
    if [ ! -f /etc/grid-services/jobmanager ]; then
        globus-gatekeeper-admin -e jobmanager-condor -n jobmanager
    fi
fi

%preun
if [ $1 -eq 0 ]; then
    globus-gatekeeper-admin -d jobmanager-condor > /dev/null 2>&1 || :
fi

%postun
if [ $1 -eq 0 -a ! -f /etc/grid-services/jobmanager ]; then
    globus-gatekeeper-admin -E > /dev/null 2>&1 || :
fi

%files -f package.filelist
%defattr(-,root,root,-)
%dir %{_datadir}/globus/packages/%{_name}
%dir %{_docdir}/%{name}-%{version}
%config(noreplace) %{_sysconfdir}/grid-services/available/jobmanager-condor
%config(noreplace) %{_sysconfdir}/osg/extattr_table.txt
%config(noreplace) %{_sysconfdir}/osg/uid_table.txt
%{perl_vendorlib}/Globus/GRAM/JobManager/condor_accounting_groups.pm
%config(noreplace) %{_sysconfdir}/globus/globus-condor.conf
%config(noreplace) %{_sysconfdir}/globus/gram/condor.rvf 

%changelog
* Mon Nov 19 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 1.0-13.4
- Fixed expression in max_wall_time patch

* Fri Nov 02 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 1.0-13.3
- Add placeholder file for user-editable condor.rvf

* Fri Oct 05 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 1.0-13.2
- Accounting groups module changes from SOFTWARE-805

* Fri Aug 17 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 1.0-13.1
- SOFTWARE-737: Mark /etc/globus/globus-condor.conf as config

* Tue Jul 24 2012 Alain Roy <roy@cs.wisc.edu> - 1.0-13
- SOFTWARE-717: Patch to work add max_wall_time RSL parameter

* Mon Jun 4 2012 Alain Roy <roy@cs.wisc.edu> - 1.0-12
- SOFTWARE-669: Patch to understand xcount and min_memory

* Mon Dec 19 2011 Matyas Selmeci <matyas@cs.wisc.edu> - 1.0-11
- Merge OSG changes

* Mon Dec 05 2011 Joseph Bester <bester@mcs.anl.gov> - 1.0-6
- Update for 5.2.0 release

* Mon Dec 05 2011 Joseph Bester <bester@mcs.anl.gov> - 1.0-5
- Last sync prior to 5.2.0

* Thu Nov 17 2011 Alain Roy <roy@cs.wisc.edu> - 1.0-10
- Fixed pathname to extattr_table.txt in Condor accounting group patch. 

* Fri Nov 4 2011 Alain Roy <roy@cs.wisc.edu> - 1.0-9
- Fixed Condor accounting group patch: missing variable assignment.

* Wed Oct 26 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 1.0-7
- Fix the location of the ea and uid tables.  Fix NFS-lite for jobs with input files.

* Thu Oct 20 2011 Joseph Bester <bester@mcs.anl.gov> - 1.0-4
- GRAM-259: globus-gram-job-manager-condor RPM does not uninstall cleanly
- Add explicit dependencies on >= 5.2 libraries

* Thu Sep 22 2011 Matyas Selmeci <matyas@cs.wisc.edu> - 1.0-5
- Fixed condition in postun scriptlet

* Thu Sep 22 2011 Joseph Bester <bester@mcs.anl.gov> - 1.0-3
- Fix: GRAM-243

* Wed Sep 21 2011 Matyas Selmeci <matyas@cs.wisc.edu> - 1.0-4
- Changed post scriptlet to only run globus-gatekeeper-admin on fresh install
so site customizations would be preserved on upgrade.

* Thu Sep 01 2011 Joseph Bester <bester@mcs.anl.gov> - 1.0-2
- Update for 5.1.2 release

* Thu Aug 18 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 0.0-4
- Fix default configuration file.

* Wed Aug 17 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 0.0-3
- Port all OSG patches to GT52.
