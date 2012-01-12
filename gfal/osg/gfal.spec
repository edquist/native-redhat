Name:		gfal
Version:	1.11.14
Release:	9
Summary:	Grid File Access Library for accessing files in multiple grid protocols

Group:		Development/Languages/C and C++
License:	Apache 2.0
URL:		http://glite.cvs.cern.ch/cgi-bin/glite.cgi/org.glite.data.gfal
# Retrieved on Sep 10 2010
# http://glite.cvs.cern.ch/cgi-bin/glite.cgi/org.glite.data.gfal.tar.gz?view=tar&pathrev=glite-data-gfal_R_1_11_14_1
Source0:        org.glite.data.gfal.tar.gz
Patch0:         gfal_makefile_cleanup.patch
Patch1:		srm.v2.2.types.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:	CGSI-gSOAP lfc-client e2fsprogs voms openldap globus-ftp-client python
BuildRequires:  automake autoconf libtool swig lfc-devel CGSI-gSOAP-devel glite-build-common-cpp voms-devel e2fsprogs-devel openldap-devel globus-ftp-client-devel python-devel

%description
%{summary}

%prep
%setup -n org.glite.data.gfal

%patch0 -p1

%build
mkdir -p src/autogen build; aclocal -I /usr/share/glite-build-common-cpp/m4/; libtoolize --force; autoheader; automake --foreign --add-missing --copy; autoconf
export CFLAGS="%{optflags} -I%{_libdir}/globus/include"
./configure --with-glite-location=/usr --with-globus-nothr-flavor=gcc64dbg --with-globus-thr-flavor=gcc64dbgpthr --with-gsoap-location=/usr --with-gsoap-version=2.7.13 --with-cgsi-gsoap-location=/usr --prefix=/usr  --with-lfc-location=/usr --with-version=%{version} --with-release=%{release}

# The patched file gets auto-generated by make, but the result is not usable.
pushd src
make srm.v2.2.h
popd
patch -p0 < %{PATCH1}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
# All the binaries are unittest stuff
rm -f $RPM_BUILD_ROOT%{_bindir}/*
rm -f $RPM_BUILD_ROOT%{_libdir}/python2.4/site-packages/*.la

# Python expects modules to be names .so, not a symlink to the real module
# So we fix them.
rm -f $RPM_BUILD_ROOT%{_libdir}/python2.4/site-packages/*.so
rm -f $RPM_BUILD_ROOT%{_libdir}/python2.4/site-packages/*.so.0
rename .so.0.0.0 .so $RPM_BUILD_ROOT%{_libdir}/python2.4/site-packages/*.so.0.0.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/lib*
%{_libdir}/python2.4/site-packages/*
%{_mandir}/man3/*
%{_docdir}/*
%{_includedir}/*

%changelog
* Thu Jan 12 2012 Alain Roy <roy@cs.wisc.edu> - 1.11.14-9
- Fixed missing Python module files

* Wed Nov 30 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 1.11.14-8
- Remove unnecessary ownership of system directories.

* Fri Oct 28 2011 Matyas Selmeci <matyas@cs.wisc.edu> - 1.11.14-7
- rebuilt

* Mon Sep 12 2011 Matyas Selmeci <matyas@cs.wisc.edu> - 1.11.14-6
- Rebuilt against updated Globus libraries

* Mon Aug 29 2011 Matyas Selmeci <matyas@cs.wisc.edu> - 1.11.14-5
- Rebuild against Globus 5.2.

* Fri Jul 15 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 1.11.14-4
- Include the correct directory for globus on 32-bit.

* Fri Jul 08 2011 Derek Weitzel <dweitzel@cse.unl.edu> 1.11.14-3
- Added the versioning in the configure command line.

* Sat Jul  2 2011 Brian Bockelman <bbockelm@cse.unl.edu> 1.11.14-1
- Update to latest release.

* Thu Sep 10 2010 Brian Bockelman <bbockelm@cse.unl.edu> 1.3.3.2-1
- Initial RPM packaging
- A few configure changes in order to force the builds to find the Fedora/EPEL
  globus libraries and includes
- Fix a few code generation errors in the SRMv2 stubs

