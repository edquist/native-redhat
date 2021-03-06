Name:      osg-gridftp-hdfs
Summary:   OSG GridFTP-HDFS meta package
Version:   3.3
Release:   4%{?dist}
License:   Apache 2.0
Group:     Grid
URL:       http://www.opensciencegrid.org

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Source1: udt-%{name}.conf

Requires: osg-version
Requires: osg-system-profiler
# 0.5.4-13 uses /etc/gridftp.d config dir
Requires: gridftp-hdfs >= 0.5.4-16
Requires: vo-client
Requires: grid-certificates >= 7
Requires: fetch-crl
Requires: gratia-probe-gridftp-transfer >= 1.17.0-1
Requires: globus-xio-udt-driver

%ifarch %{ix86}
Requires: liblcas_lcmaps_gt4_mapping.so.0
%else
Requires: liblcas_lcmaps_gt4_mapping.so.0()(64bit)
%endif

%description
This is a meta package for a standalone GridFTP server with 
HDFS and GUMS support.

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/gridftp.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gridftp.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/gridftp.d/udt-%{name}.conf

%changelog
* Thu Aug 25 2016 Carl Edquist <edquist@cs.wisc.edu> - 3.3-4
- drop gums-client dependency (SOFTWARE-2398)
- remove rhel5-specific macros (OSG-3.2 EOL)

* Tue Feb 09 2016 Carl Edquist <edquist@cs.wisc.edu> - 3.3-3
- Remove gums-client requirement for EL7 (SOFTWARE-2176)

* Wed Jul 01 2015 Mátyás Selmeci <matyas@cs.wisc.edu> 3.3-2
- Require grid-certificates >= 7 (SOFTWARE-1883)

* Wed Apr 29 2015 Mátyás Selmeci <matyas@cs.wisc.edu> 3.3-1
- Rebuild for OSG 3.3

* Thu Apr 03 2014 Carl Edquist <edquist@cs.wisc.edu> - 3.0.0-6
- Add version requirement for gridftp-hdfs (SOFTWARE-1412)

* Thu Mar 13 2014 Carl Edquist <edquist@cs.wisc.edu> - 3.0.0-4
- Add globus-xio-udt-driver dependency for el6, and enable by default in
  /etc/gridftp.d/ (SOFTWARE-1412)

* Fri Feb 22 2013 Brian Lin <blin@cs.wisc.edu> - 3.0.0-3
- Update rhel5 to require fetch-crl3 instead of fetch-crl.

* Mon Nov 14 2011 Alain Roy <roy@cs.wisc.edu> - 3.0.0-2
- Added dependencies on osg-version and osg-system-profiler

* Sat Sep 24 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 3.0.0-1
- Initial creation of meta-package for gridftp-hdfs.

