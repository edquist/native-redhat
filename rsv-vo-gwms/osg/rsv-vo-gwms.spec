Name:      rsv-vo-gwms
Version:   1.1.0
Release:   1%{?dist}
Summary:   RSV metrics to test CE's from gwms factory
Packager:  OSG-Software
Group:     Applications/Monitoring
License:   Apache 2.0
URL:       https://twiki.grid.iu.edu/bin/view/MonitoringInformation/RSV

Source0:   %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: rsv >= 3.13
Requires: condor-python


%description
%{summary}

%prep
%setup -n %{name}-%{version}
#%setup -n %{version}

%install
rm -fr $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%defattr(-,root,root,-)
%{_libexecdir}/rsv/probes/gfactory-querying-local-probe
%{_libexecdir}/rsv/probes/dummy-probe
%{_libexecdir}/rsv/metrics/org.osg.general.dummy-probe
%{_libexecdir}/rsv/metrics/org.osg.local-gfactory-querying-local
%config %{_sysconfdir}/rsv/meta/metrics/org.osg.local-gfactory-querying-local.meta
%config(noreplace) %{_sysconfdir}/rsv/metrics/org.osg.local-gfactory-querying-local.conf
%attr(-,rsv,rsv)  %{_sysconfdir}/rsv
%attr(-,rsv,rsv)  %{_sysconfdir}/rsv/metrics
%attr(755, -, -) %{_libexecdir}/rsv/metrics/org.osg.local-gfactory-querying-local
%attr(755, -, -) %{_libexecdir}/rsv/probes/gfactory-querying-local-probe

%post -p /bin/bash


%changelog
* Thu May 26 2016 <efajado@physics.ucsd.edu> - 1.1.0-1
- Added the dummy probe to be able to test CREAM and Nordugrid sites
- Removed the logrotate files since they were not needed

* Fri Mar 13 2015 <efajardo@physics.ucsd.edu> - 1.0.1-1
- Changed the defaults to query CMS sites

* Thu Jan 29 2015 <efajardo@physics.ucsd.edu> - 1.0.0-1
- Tagged version 1.0.0

* Tue Jan 27 2015 <efajardo@physics.ucsd.edu> - 0.0.2-1
- Bumped to version 0.0.2

* Tue Jan 27 2015 <efajardo@physics.ucsd.edu> - 0.0.1-3
- Fixed permissions on local probe

* Wed Nov 14 2014 <efajardo@physics.ucsd.edu> - 0.0.1-2
- Fixed the requires condor-python

* Wed Nov 14 2014 <efajardo@physics.ucsd.edu> - 0.0.1-1
- Creating a first RPM for rsv-vo-gwms
