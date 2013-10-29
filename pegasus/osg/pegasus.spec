Name:           pegasus
Version:        4.2.0
Release:        1.2%{?dist}
Summary:        Workflow management system for Condor, grids, and clouds
Group:          Applications/System
License:        ASL 2.0
URL:            http://pegasus.isi.edu/
Packager:       Mats Rynge <rynge@isi.edu>

Source:         pegasus-source-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-root
BuildRequires:  ant, ant-apache-regexp, java7-devel, gcc, groff, python-devel, gcc-c++, make
BuildRequires:  jpackage-utils
# ensure these are present, from jpackage-utils or missing-java-1.7.0-dirs
Requires: /usr/lib/java-1.7.0
Requires: /usr/share/java-1.7.0

Requires:       java7 >= 1:1.7.0, jpackage-utils, python >= 2.4, condor >= 7.6, graphviz

%define sourcedir %{name}-source-%{version}

%description
The Pegasus project encompasses a set of technologies that
help workflow-based applications execute in a number of
different environments including desktops, campus clusters,
grids, and now clouds. Scientific workflows allow users to
easily express multi-step computations. Once an application
is formalized as a workflow the Pegasus Workflow Management
Service can map it onto available compute resources and
execute the steps in appropriate order.


%prep
%setup -q -n %{sourcedir}


%build
export CLASSPATH=$(build-classpath ant)
ant dist

# strip executables
strip dist/pegasus-%{version}/bin/pegasus-invoke
strip dist/pegasus-%{version}/bin/pegasus-cluster
strip dist/pegasus-%{version}/bin/pegasus-kickstart
strip dist/pegasus-%{version}/bin/pegasus-keg

# fix pegasus-config on 64 bit systems
if (echo %{_libdir} | grep lib64); then 
    perl -p -i -e 's/^my \$lib.*/my \$lib         = "lib64";/' \
         dist/pegasus-%{version}/bin/pegasus-config
fi

%install
rm -Rf %{buildroot}

mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_datadir}

cp -aR dist/pegasus-%{version}/etc/* %{buildroot}/%{_sysconfdir}/%{name}/
cp -aR dist/pegasus-%{version}/bin/* %{buildroot}/%{_bindir}/
cp -aR dist/pegasus-%{version}/lib/* %{buildroot}/%{_libdir}/
cp -aR dist/pegasus-%{version}/share/* %{buildroot}/%{_datadir}/

# rm unwanted files
rm -f %{buildroot}/%{_bindir}/keg.condor
rm -f %{buildroot}/%{_datadir}/%{name}/java/COPYING.*
rm -f %{buildroot}/%{_datadir}/%{name}/java/EXCEPTIONS.*
rm -f %{buildroot}/%{_datadir}/%{name}/java/LICENSE.*
rm -f %{buildroot}/%{_datadir}/%{name}/java/NOTICE.*


%clean
ant clean
rm -Rf %{buildroot}


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/*
%{_libdir}/%{name}/
%{_datadir}/doc/%{name}
%{_datadir}/man/man1/*
%{_datadir}/%{name}


%changelog
* Tue May 07 2013 Carl Edquist <edquist@cs.wisc.edu> - 4.2.0-1.2
- Require missing java dir names instead of workaround package

* Tue Apr 09 2013 Brian Lin <blin@cs.wisc.edu> 4.2.0-1.1
- Change dependencies to use and build against java7

* Fri Jan 11 2013 Mats Rynge <rynge@isi.edu> 4.2.0
- 4.2.0 release

* Tue Feb 7 2012 Mats Rynge <rynge@isi.edu> 4.1.0
- 4.1.0 release

* Tue Feb 7 2012 Mats Rynge <rynge@isi.edu> 4.0.0cvs-1
- Preparing for 4.0.0
- Added graphviz-gd as dep

* Mon Aug 29 2011 Mats Rynge <rynge@isi.edu> 3.2.0cvs-1
- Moved to 3.2.0cvs which is FHS compliant

* Fri Jul 22 2011 Doug Strain <dstrain@fnal.gov> 3.0.3-2
- Fixing common.pm
- Adding g++ to dependencies

* Wed Jul 20 2011 Doug Strain <dstrain@fnal.gov> 3.0.3-1
- Initial creation of spec file
- Installs into /usr/share/pegasus-3.0.3
- Binaries into /usr/bin


