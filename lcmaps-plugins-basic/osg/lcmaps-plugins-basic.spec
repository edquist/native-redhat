Summary: Basic plugins for the LCMAPS authorization framework
Name: lcmaps-plugins-basic
Version: 1.5.1
Release: 2.1%{?dist}
License: ASL 2.0
Group: System Environment/Libraries
URL: http://wiki.nikhef.nl/grid/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRequires: lcmaps-interface
BuildRequires: openldap-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: lcmaps%{?_isa} >= 1.5.0

%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the basic plugins.

%package ldap
Summary: LDAP enforcement plug-in for LCMAPS
Group: System Environment/Libraries
Requires: lcmaps%{?_isa} >= 1.5.0

%description ldap
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the LDAP enforcement plug-in.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/lcmaps/lcmaps_ban_dn.mod
%{_libdir}/lcmaps/lcmaps_dummy_bad.mod
%{_libdir}/lcmaps/lcmaps_dummy_good.mod
%{_libdir}/lcmaps/lcmaps_localaccount.mod
%{_libdir}/lcmaps/lcmaps_poolaccount.mod
%{_libdir}/lcmaps/lcmaps_posix_enf.mod
%{_libdir}/lcmaps/liblcmaps_ban_dn.so
%{_libdir}/lcmaps/liblcmaps_dummy_bad.so
%{_libdir}/lcmaps/liblcmaps_dummy_good.so
%{_libdir}/lcmaps/liblcmaps_localaccount.so
%{_libdir}/lcmaps/liblcmaps_poolaccount.so
%{_libdir}/lcmaps/liblcmaps_posix_enf.so
%{_mandir}/man8/lcmaps_ban_dn.mod.8*
%{_mandir}/man8/lcmaps_dummy_bad.mod.8*
%{_mandir}/man8/lcmaps_dummy_good.mod.8*
%{_mandir}/man8/lcmaps_localaccount.mod.8*
%{_mandir}/man8/lcmaps_poolaccount.mod.8*
%{_mandir}/man8/lcmaps_posix_enf.mod.8*
%doc AUTHORS LICENSE

%files ldap
%defattr(-,root,root,-)
%{_libdir}/lcmaps/lcmaps_ldap_enf.mod
%{_libdir}/lcmaps/liblcmaps_ldap_enf.so
%{_mandir}/man8/lcmaps_ldap_enf.mod.8*
%doc AUTHORS LICENSE

%changelog
* Wed Dec 26 2012 Dave Dykstra <dwd@fnal.gov> 1.5.1-2.1.osg
- Import 1.5.1-2 from upstream
- Eliminate support for backward-compatible symlink at %{_libdir}/modules

* Tue Oct 23 2012 Mischa Salle <msalle@nikhef.nl> 1.5.1-2
- Add minimal lcmaps version.
- Remove configure flag for moduledir.

- Added plugin lcmaps_ban_dn including manpage.
- Update URL.
- Add run-time requirement for lcmaps for basic package.
- Add architecture to run-time requirement for ldap subpackage.
- Updated version

* Thu Mar 08 2012 Dave Dykstra <dwd@fnal.gov> 1.5.0-3.2.osg
- Rebuild after merge into trunk from branches/lcmaps-upgrade

* Tue Feb 28 2012 Dave Dykstra <dwd@fnal.gov> 1.5.0-3.1.osg
- Imported the changelog entries for 1.5.0-2 and 1.5.0-3.  All the
  actual changes had already in effect been done.

* Wed Jan 5 2012 Dave Dykstra <dwd@fnal.gov> 1.5.0-1.3.osg
- Another rebuild, trying to get the koji tags & targets right

* Wed Jan 4 2012 Dave Dykstra <dwd@fnal.gov> 1.5.0-1.2.osg
- Just rebuilding

* Fri Dec 30 2011 Dave Dykstra <dwd@fnal.gov> 1.5.0-1.1.osg
- Imported to 1.5.0-1 to OSG
- Moved moduledir up to libdir/lcmaps instead of libdir/lcmaps/plugins
- Added %ghost rules for the corresponding files in libdir/modules
  because OSG has a symlink there

* Thu Dec 27 2011 Oscar Koeroo <okoeroo@nikhef.nl> 1.5.0-3
- Changed the install directory to libdir/lcmaps/ for the LDAP plugin.

* Thu Dec 23 2011 Oscar Koeroo <okoeroo@nikhef.nl> 1.5.0-2
- Changed the install directory to libdir/lcmaps/ for the plugins.

* Thu Dec 15 2011 Mischa Salle <msalle@nikhef.nl> 1.5.0-1
- updated version

* Wed Nov 16 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.6-2
- moved plugin to plugins/ subdirectory

* Thu Jul 14 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.6-1
- Updated version

* Tue Jul  5 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.4.5-2
- Remove Vendor tag

* Thu Jun 30 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.5-1
- Moved lcmaps_ldap_enf.mod to the -ldap package
- Updated to version 1.4.5

* Wed Apr  6 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.3-1
- bumped version

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.2-4
- removed explicit requires

* Mon Mar  7 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.2-3
- Split off the ldap enforcement plug-in

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.2-2
- drop the development package
- fixed the licence string

* Mon Feb 21 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.