Summary: SCAS client plugin for the LCMAPS authorization framework
Name: lcmaps-plugins-scas-client
Version: 0.3.0
Release: 1.1%{?dist}
Vendor: Nikhef
License: ASL 2.0
Group: System Environment/Libraries
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
Patch0: memory_corruption.patch
Patch1: ca_only.patch
Patch2: fix_loglevels.patch
BuildRequires: openssl-devel
BuildRequires: lcmaps-interface, saml2-xacml2-c-lib-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the SCAS client plug-in. This LCMAPS plugin
functions as the PEP (client side) implementation to an Site Central
Authorization Service (SCAS) or GUMS (new style) service.

%package -n lcmaps-plugins-saz-client
Group: System Environment/Libraries
Obsoletes: lcmaps-plugins-saz
Summary: SAZ support for lcmaps

%description -n lcmaps-plugins-saz-client
%{summary}

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# the module must be a copy, not a symlink, because the gums-client
#  is a symlink and lcmaps can't use the same module file twice
cp $RPM_BUILD_ROOT%{_libdir}/lcmaps/lcmaps_scas_client.mod $RPM_BUILD_ROOT%{_libdir}/lcmaps/lcmaps_saz_client.mod
cp $RPM_BUILD_ROOT%{_datadir}/man/man8/lcmaps_plugins_scas_client.8 $RPM_BUILD_ROOT%{_datadir}/man/man8/lcmaps_plugins_saz_client.8

# This symlink is here for backward-compatible %ghost files
ln -s lcmaps $RPM_BUILD_ROOT%{_libdir}/modules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS  LICENSE
%{_libdir}/lcmaps/lcmaps_scas_client.mod
%{_libdir}/lcmaps/liblcmaps_scas_client.so
%{_datadir}/man/man8/lcmaps_plugins_scas_client.8.gz
%ghost %{_libdir}/modules
%ghost %{_libdir}/modules/lcmaps_scas_client.mod
%ghost %{_libdir}/modules/liblcmaps_scas_client.so

%files -n lcmaps-plugins-saz-client
%{_libdir}/lcmaps/lcmaps_saz_client.mod
%{_datadir}/man/man8/lcmaps_plugins_saz_client.8.gz
%ghost %{_libdir}/modules/lcmaps_saz_client.mod

%changelog
* Fri Dec 30 2011 Dave Dykstra <dwd@fnal.gov> 0.3.0-1.1.osg
- Imported into OSG
- Added "Requires: saml2-xacml2-c-lib", instead of the implicit
    requirement of libxaml.so which sometimes instead picks up
    prima from hadoop repo
- Included ca_only.patch to fix a SEGV when no user certificate is present.
- Included memory_corrupt.patch to fix a memory corruption issue on an
    error condition.
- Added fix_loglevels.patch to complete conversion to new lcmaps_log levels
- Added subpackage lcmaps-plugins-saz-client
- Added %ghost for plugin files in modules directory so they won't
   get deleted in an upgrade (since modules is now a symlink).

* Fri Dec 16 2011 Mischa Salle <msalle@nikhef.nl> 0.3.0-1
- bumped version
- updated installation dir plugins and removed .so.0* files

* Wed Apr  6 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.2.22-1
- bumped version

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.2.21-2
- removed explicit requires

* Mon Mar  7 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.2.21-1
- added openssl dependency

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.2.20-2
- fixed license string
- dropped devel package
- disable static libraries

* Mon Feb 21 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.


