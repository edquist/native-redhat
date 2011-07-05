Name:		glite-data-delegation-api-c
Version:	2.0.0.7
Release:	1
Summary:	Library for using the gLite delegation API from C

Group:		Development/Languages/C and C++
License:	Apache 2.0
URL:		http://glite.cvs.cern.ch/cgi-bin/glite.cgi/org.glite.data.delegation-api-c
# Retrieved on Jul 5 2011
# http://glite.cvs.cern.ch/cgi-bin/glite.cgi/org.glite.data.delegation-api-c.tar.gz?view=tar&pathrev=glite-data-delegation-api-c_R_2_0_0_7
Source0:        org.glite.data.delegation-api-c.tar.gz
Source1:        stdsoap2.c
Patch0:         glite_data_delegation_api_c_fedora.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  automake autoconf libtool
BuildRequires:  CGSI-gSOAP-devel
BuildRequires:  glite-build-common-cpp
BuildRequires:  glite-security-delegation-interface
BuildRequires:  glite-data-build
BuildRequires:  globus-gsi-proxy-core-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gsi-credential-devel

%description
%{summary}

%prep
%setup -n org.glite.data.delegation-api-c

%patch0 -p0
cp %{SOURCE1} .

%build
./bootstrap

# Note the gsoap version is hardcoded.  The true gsoap version doesn't matter, only that it is greater than 2.3
%configure --with-delegation-wsdl=/usr/share/glite-security-delegation-interface/interface/www.gridsite.org-delegation-2.0.0.wsdl --with-gsoap-version=2.7.13 --with-interface-version=2.0.0

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
# All the binaries are unittest stuff
rm -f $RPM_BUILD_ROOT%{_bindir}/*
rm -f $RPM_BUILD_ROOT%{_libdir}/python2.4/site-packages/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/python2.4/site-packages/*.so.0.0.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*
%{_docdir}/glite-data-delegation-api-c
%{_includedir}/glite/data/delegation

%changelog
* Sat Jul  2 2011 Brian Bockelman <bbockelm@cse.unl.edu> 1.11.14-1
- Update to latest release.

* Thu Sep 10 2010 Brian Bockelman <bbockelm@cse.unl.edu> 1.3.3.2-1
- Initial RPM packaging
- A few configure changes in order to force the builds to find the Fedora/EPEL
  globus libraries and includes
- Fix a few code generation errors in the SRMv2 stubs

