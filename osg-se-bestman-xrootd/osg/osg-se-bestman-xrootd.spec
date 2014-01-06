Name:           osg-se-bestman-xrootd
Summary:        OSG BeStMan XRootd Storage Element package
Version:        3.0.0
Release:        6%{?dist}
License:        GPL
Group:          System Environment/Daemons
URL:            https://twiki.grid.iu.edu/twiki/bin/view/Storage/WebHome

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# from VDT
Requires: osg-version
Requires: osg-system-profiler
Requires: bestman2-server
Requires: bestman2-client
Requires: bestman2-tester
Requires: edg-mkgridmap
%if 0%{?rhel} < 6
Requires: fetch-crl3
%else
Requires: fetch-crl
%endif
# From osg-gridftp meta package
Requires: globus-gridftp-server-progs
Requires: vo-client
Requires: grid-certificates
Requires: gratia-probe-gridftp-transfer
Requires: gums-client
%ifarch %{ix86}
Requires: liblcas_lcmaps_gt4_mapping.so.0
%else
Requires: liblcas_lcmaps_gt4_mapping.so.0()(64bit)
%endif

#Xrootd stuff
Requires: xrootd-dsi
Requires: xrootd-fuse
Requires: gratia-probe-xrootd-transfer
Requires: gratia-probe-xrootd-storage


%description
This is a meta-package for the BeStMan (Berkeley Storage Manager)
with underlying xrootd storage element using fuse/dsi module.

%install

%clean
rm -rf $RPM_BUILD_ROOT

%files


%changelog
* Thu Apr 04 2013 Brian Lin <blin@cs.wisc.edu> - 3.0.0-6
- Remove java dependency.

* Fri Feb 22 2013 Brian Lin <blin@cs.wisc.edu> - 3.0.0-5
- Update rhel5 to require fetch-crl3 instead of fetch-crl.

* Mon Nov 14 2011 Alain Roy <roy@cs.wisc.edu> - 3.0.0-4
- Added dependencies on osg-version and osg-system-profiler

* Wed Sep 28 2011 Doug Strain <dstrain@fnal.gov> - 3.0.0-3
- This meta package should not be noarch due to lib dependencies

* Thu Sep 1 2011 Doug Strain <dstrain@fnal.gov> - 3.0.0-1
- Initial creation of osg-se-bestman-xrootd meta package