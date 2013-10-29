%global name osg-configure
%global version 1.0.47
%global release 1%{?dist}

Summary: Package for configure-osg and associated scripts
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: Apache 2.0
Group: Grid
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Suchandra Thapa <sthapa@ci.uchicago.edu>
Url: http://www.opensciencegrid.org
Requires: python 
Requires: yum
Provides: osg-configure

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%description
%{summary}

%package rsv
Summary: Configure-osg configuration files for rsv
Group: Grid
Provides: configure-osg-rsv
Requires: %name = %version-%release
%description rsv
This package includes the ini file for configuring rsv using configure-osg
%package cemon
Summary: Configure-osg configuration files for cemon
Group: Grid
Provides: configure-osg-cemon
Requires: %name = %version-%release
%description cemon
This package includes the ini file for configuring cemon using configure-osg
%package gratia
Summary: Configure-osg configuration files for gratia
Group: Grid
Provides: configure-osg-gratia
Requires: %name = %version-%release
%description gratia
This package includes the ini file for configuring gratia using configure-osg
%package gip
Summary: Configure-osg configuration files for gip
Group: Grid
Provides: configure-osg-gip
Requires: %name = %version-%release
%description gip
This package includes the ini file for configuring gip using configure-osg
%package lsf
Summary: Configure-osg configuration files for lsf
Group: Grid
Provides: configure-osg-lsf
Requires: %name = %version-%release
%description lsf
This package includes the ini file for configuring lsf using configure-osg
%package pbs
Summary: Configure-osg configuration files for pbs
Group: Grid
Provides: configure-osg-pbs
Requires: %name = %version-%release
%description pbs
This package includes the ini file for configuring pbs using configure-osg
%package condor
Summary: Configure-osg configuration files for condor
Group: Grid
Provides: configure-osg-condor
Requires: %name = %version-%release
%description condor
This package includes the ini file for configuring condor using configure-osg
%package sge
Summary: Configure-osg configuration files for sge
Group: Grid
Provides: configure-osg-sge
Requires: %name = %version-%release
%description sge
This package includes the ini file for configuring sge using configure-osg
%package monalisa
Summary: Configure-osg configuration files for monalisa
Group: Grid
Provides: configure-osg-monalisa
Requires: %name = %version-%release
%description monalisa
This package includes the ini files for configuring monalisa
%package ce
Summary: Configure-osg configuration files for CE
Group: Grid
Provides: configure-osg-ce
Requires: %name = %version-%release
%description ce
This package includes the ini files for configuring a basic CE using 
configure-osg.  One of the packages for the job manager configuration also 
needs to be installed for the CE configuration.
%package misc
Summary: Configure-osg configuration files for misc software
Group: Grid
Provides: configure-osg-misc
Requires: %name = %version-%release
%description misc
This package includes the ini files for various osg software including
certificates setup and glexec
%package squid
Summary: Configure-osg configuration files for squid
Group: Grid
Provides: configure-osg-squid
Requires: %name = %version-%release
%description squid
This package includes the ini files for configuring an OSG system to use squid
%package managedfork
Summary: Configure-osg configuration files for managedfork
Group: Grid
Provides: configure-osg-managedfork
Requires: %name = %version-%release
%description managedfork
This package includes the ini files for configuring an OSG CE to use
managedfork 
%package network
Summary: Configure-osg configuration files for network configuration
Group: Grid
Provides: configure-osg-network
Requires: %name = %version-%release
%description network
This package includes the ini files for configuring network related information
such as firewall ports that globus should use
%package tests
Summary: Configure-osg configuration unit tests and configuration for unit testing
Group: Grid
Provides: configure-osg-tests
Requires: %name = %version-%release
%description tests
This package includes the ini files and files for unit tests that osg-configure
uses to verify functionality
%package slurm
Summary: Configure-osg configuration files for slurm
Group: Grid
Provides: configure-osg-slurm
Requires: %name = %version-%release
%description slurm
This package includes the ini file for configuring slurm using configure-osg

%prep
%setup

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/log/osg/
touch $RPM_BUILD_ROOT/var/log/osg/osg-configure.log
mkdir -p $RPM_BUILD_ROOT/var/lib/osg
touch $RPM_BUILD_ROOT/var/lib/osg/osg-attributes.conf
touch $RPM_BUILD_ROOT/var/lib/osg/osg-local-job-environment.conf
touch $RPM_BUILD_ROOT/var/lib/osg/osg-job-environment.conf
touch $RPM_BUILD_ROOT/var/lib/osg/globus-firewall
mkdir -p $RPM_BUILD_ROOT/etc/profile.d/
touch $RPM_BUILD_ROOT/etc/profile.d/osg.sh
touch $RPM_BUILD_ROOT/etc/profile.d/osg.csh
# following is needed to move script to sbin directory
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mv $RPM_BUILD_ROOT/usr/bin/osg-configure $RPM_BUILD_ROOT/usr/sbin/osg-configure
ln -s /usr/sbin/osg-configure $RPM_BUILD_ROOT/usr/sbin/configure-osg 
rmdir $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%{python_sitelib}/*
/usr/sbin/*
%ghost /var/log/osg/osg-configure.log
%ghost /var/lib/osg/osg-attributes.conf
%ghost /var/lib/osg/osg-local-job-environment.conf
%ghost /var/lib/osg/osg-job-environment.conf

%files rsv
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/30-rsv.ini
%files cemon
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/30-cemon.ini
%files gratia
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/30-gratia.ini
%files gip
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/30-gip.ini
%files lsf
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/20-lsf.ini
%files pbs
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/20-pbs.ini
%files condor
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/20-condor.ini
%files sge
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/20-sge.ini
%files ce
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/40-localsettings.ini
%config(noreplace) %{_sysconfdir}/osg/config.d/40-siteinfo.ini
%config(noreplace) %{_sysconfdir}/osg/config.d/10-storage.ini
%config(noreplace) %{_sysconfdir}/osg/grid3-locations.txt
%files misc
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/10-misc.ini
%files squid
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/01-squid.ini
%files monalisa
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/02-monalisa.ini
%files managedfork
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/15-managedfork.ini
%files network
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/40-network.ini
%ghost /var/lib/osg/globus-firewall
%ghost %{_sysconfdir}/profile.d/osg.sh
%ghost %{_sysconfdir}/profile.d/osg.csh
%files tests
%defattr(-,root,root)
/usr/share/osg-configure/*
%files slurm
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/osg/config.d/20-slurm.ini

%changelog
* Thu Oct 24 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.47-1
- Fix for hostname identification on CentOS 6
- Fixes for bugs in condor-cron id fixes

* Thu Oct 17 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.46-1
- Allow sge binary location to be specified
- Give better error messages when options are missing
- Add requires in sub-rpms for osg-configure main rpm
- Check and fix condor-cron ids for RSV

* Wed Sep 16 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.45-1
- Update unit tests for http proxy validation

* Wed Sep 16 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.44-1
- Change http proxy validation per dicussions with Brian and Tim

* Wed Sep 9 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.43-1
- Fix gratia configuration errors for slurm configuration
- Update squid location checks 

* Wed Sep 9 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.42-1
- Fix gratia configuration errors for slurm/sge

* Wed Sep 4 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.41-1
- Added missing config files for unit tests
- Temporarily disable unit test for unused functionality

* Tue Sep 3 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.40-1
- Fix gratia condor probe configuration
- Fix breakage when variable substitution across files or bad variable
  substitution is present
- Add unit tests for above issue

* Thu Aug 29 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.39-1
- Fix squid unit test

* Thu Aug 29 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.38-1
- Add unit tests for squid location check
- Fixes for squid location check

* Fri Aug 23 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.37-1
- Unit test fixes
- Test squid location

* Mon Aug 19 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.36-1
- Multiple bug fixes
- Add Slurm gratia support

* Mon Aug 5 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.35-1
- Fix error message when ram_mb is too high

* Fri Aug 2 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.34-1
- Add unit tests for spaces in ini files

* Thu Aug 1 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.33-1
- Fixes for lines with spaces at beginning of sections in ini files
- Increase the allowed memory to 512GB per node in GIP sanity checks

* Thu Apr 25 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.30-1
- Remove duplicate and broken check for SGE log files

* Tue Apr 9 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.29-1
- Fix SGE unit test errors

* Tue Apr 9 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.28-1
- Fix SGE verification issue 
- Removed stray character in 20-lsf.ini file

* Fri Apr 5 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.27-1
- More fixes for LSF gratia probe configuration

* Fri Mar 29 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.26-1
- Fixes for LSF gratia probe configuration

* Thu Mar 28 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.25-1
- Use log_directory for LSF instead of accounting_log_directory

* Wed Mar 27 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.24-1
- Added support for configuring gratia LSF module

* Wed Mar 19 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.23-1
- Added multiple fixes for LSF

* Wed Feb 20 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.22-1
- Added support for fetch-crl3 if present

* Mon Feb 04 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.21-1
- Added support for SLURM and unit tests for SLURM

* Thu Jan 10 2013 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.20-1
- Multiple clean ups in unit tests
- Add --enabled-services argument to retun a list of services configured

* Tue Dec 04 2012 Suchandra Thapa <sthapa@ci.uchicago.edu>  1.0.19-1
- Fix localsettings configuration (add getAttributes back)
- Fix gratia unit tests due to change in test configs
- Clean up unit test code based on pylint output

* Tue Dec 04 2012 Suchandra Thapa <sthapa@ci.uchicago.edu>  1.0.18-1
- Don't configure metric probe in gratia test configs

* Tue Dec 04 2012 Suchandra Thapa <sthapa@ci.uchicago.edu>  1.0.17-1
- Fix for SOFTWARE-859 / GOC-12974 
- Multiple cleanups and fixes based on pylint analysis

* Thu Nov 15 2012 Suchandra Thapa <sthapa@ci.uchicago.edu>  1.0.16-1
- Fixes for software-811, software-834 
- Code cleanups based on pylint

* Thu Aug 08 2012 Suchandra Thapa <sthapa@ci.uchicago.edu>  1.0.15-1
- Update tests for storage
- Incorporate SGE fixes
- Add support for sites without OSG_DATA or which dynamically set OSG_WN_TMP
- Fix various bugs reported by Patrick @ UTA

* Thu Jun 14 2012 Suchandra Thapa <sthapa@ci.uchicago.edu>  1.0.14-1
- Update tests and fix some minor bugs

* Thu Jun 14 2012 Suchandra Thapa <sthapa@ci.uchicago.edu>  1.0.13-1
- Fix network state file checking
- Update logging in unit tests

* Fri Jun 8 2012 Suchandra Thapa <sthapa@ci.uchicago.edu>  1.0.12-1
- Include a few test related changes that were accidentally left out of the
  previous release

* Fri Jun 8 2012 Suchandra Thapa <sthapa@ci.uchicago.edu>  1.0.11-1
- Allow WN_TMP to be left blank
- Don't require globus port state files to be present
- Updates to test packaging and cleanups

* Mon Jun 4 2012 Scot Kronenfeld <kronenfe@cs.wisc.edu> 1.0.10-1
- Don't try to get rsv user uid, gid in __init__

* Fri Jun 1 2012 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.8-1
- Multiple fixes

* Wed May 2 2012 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.8-1
- Fix for SOFTWARE-597
- Fix for SOFTWARE-599 
- Added tests subpackage to distribute tests
- Added fixes for gip configuration issue Alain ran into

* Mon Apr 23 2012 Alain Roy <roy@cs.wisc.edu> 1.0.7-2
- Patched to fix SOFTWARE-637 (incorrectly setting accounting dir for PBS)
- Added proper setup for Gratia Metric probe -SWK
- Added new RSV option - legacy_proxy -SWK

* Wed Mar 14 2012 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.7-1
- Fix for Software-552
- Implemented Software-568
- Fixes and changes suggested by Alain
- Unit test updates

* Wed Feb 29 2012 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.6-1
- Add support for configuring gratia condor and pbs probes
- Fix missing newline in message when -d is used

* Thu Feb 23 2012 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.5-1
- Cleaned up pbs and lsf config scripts to remove unused home settings
- Removed itb entries from cemon ini file
- Fixed gip errors when on a standalone RSV install

* Tue Feb 21 2012 Scot Kronenfeld <kronenfe@cs.wisc.edu> 1.0.4-1
- Fixed a bug in RSV configuration that prevented the use of user proxies.

* Fri Jan 27 2012 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.3-1
- Minor tweak to let configuration continue if grid3-locations isn't present
- Remove seg_enabled option from condor jobmanager section, it's not used or
  supported by globus condor lrm

* Fri Jan 20 2012 Scot Kronenfeld <kronenfe@cs.wisc.edu> 1.0.2-1
- Minor bug fix for condor_location knob in 30-rsv.ini

* Fri Jan 20 2012 Scot Kronenfeld <kronenfe@cs.wisc.edu> 1.0.1-1
- Added condor_location knob for RSV to specify non-standard installs.

* Tue Jan 17 2012 Suchandra Thapa <sthapa@ci.uchicago.edu> 1.0.0-1
- Added support for network/firewall configuration
- Improved error reporting 
- Bug fixes for error reporting

* Wed Jan 11 2012 Scot Kronenfeld <kronenfe@cs.wisc.edu> 0.7.4-1
- Added configuration for osg-cleanup scripts

* Thu Jan 05 2012 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.7.3-1
- Added support for globus job manager config
- Added support for updating lcmaps.db and gums-client.properties files
- Added support for configuring SEG for job managers that support it
- Improved error reporting
- Internal refactoring done to improve maintainability

* Fri Dec 30 2011 Scot Kronenfeld <kronenfe@cs.wisc.edu> 0.7.2-1
- Improved RSV configuration

* Wed Dec 7 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.7.1-1
- Fix the default location of the condor_config file
- Update ini comments to point to correct documentation

* Mon Dec 1 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.7.0-1
- Fix fetching VO names from user-vo-map file

* Mon Nov 21 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.6.9-1
- Update defaults for rsv certs

* Thu Nov 17 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.6.8-1
- Fix bugs in configuring gratia probes

* Mon Nov 8 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.6.7-1
- Update to 0.6.7 to incorporate a variety of bug fixes
- Add support for configuring authentication methods

* Mon Oct 31 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.6.6-1
- Update to 0.6.6 to fix setting default job manager
- Update config files to use DEFAULT instead of UNAVAILABLE where appropriate

* Wed Oct 26 2011 Scot Kronenfeld <kronenfe@cs.wisc.edu> 0.6.5-1
- Fixed a few RSV configuration issues.

* Tue Oct 25 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.6.4-1
- Writing to osg attributes file and update to 0.6.4

* Fri Oct 21 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.6.3-1
- Fix a few bugs and update to 0.6.3

* Fri Oct 21 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.6.2-1
- Added support for accept_limited in all job managers

* Thu Oct 20 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.6.1-1
- Added bugfixes dealing with managed fork configuration

* Thu Oct 20 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.6.0-1
- Added configuration of globus job manager for managed fork 
- Fixed unit tests for RSV

* Mon Oct 10 2011 Matyas Selmeci <matyas@cs.wisc.edu> 0.5.10-1
- Added configuration of glite-ce-monitor

* Mon Sep 26 2011 Scot Kronenfeld <kronenfe@cs.wisc.edu> 0.5.8-1
- Fixed a bug in RSV configuration of gridftp hosts

* Tue Sep 13 2011 Scot Kronenfeld <kronenfe@cs.wisc.edu> 0.5.7-1
- Fixed a bug in RSV configuration of Gratia Metric ProbeConfig

* Fri Sep 09 2011 Scot Kronenfeld <kronenfe@cs.wisc.edu> 0.5.5-1
- Fixed a bug in rsv configuration when meta directory is not present

* Thu Sep 8 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> - 0.5.4-1
- Update to 0.5.4
- Add more subpackages for config files

* Mon Aug 26 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> - 0.5.2-1
- Update to 0.5.2
- Let config files reside in /etc/osg/config.d
- Make output files in /var/lib/osg ghost files

* Mon Aug 1 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> - 0.5.1-1
- Update to 0.5.1
- Add symlink for config.ini
- Make output files in /var/lib/osg ghost files

* Mon Jul 25 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> - 0.5.0-1
- Update to 0.5.0

* Mon Jul 25 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> - 0.0.4-1
- Update to 0.0.4

* Mon Jul 25 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> - 0.0.3-1
- Update to 0.0.3
- Fix python_sitelab declaration
- Use %{__python} instead of python

* Fri Jul  22 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.0.2-2
- Include .pyo files in files

* Fri Jul  22 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.0.2-1
- Created initial configure-osg rpm using real source 

* Thu Jul  21 2011 Suchandra Thapa <sthapa@ci.uchicago.edu> 0.0.1-1
- Created an initial osg-configure RPM 