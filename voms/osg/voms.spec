%if %{?fedora}%{!?fedora:0} >= 9
%global withjava 1
%else
%if %{?rhel}%{!?rhel:0} >= 5
%ifarch %{ix86} x86_64
%global withjava 1
%else
%global withjava 0
%endif
%else
%global withjava 0
%endif
%endif

%if %{?fedora}%{!?fedora:0} >= 16 || %{?rhel}%{!?rhel:0} >= 7
%global compat 0
%else
%global compat 1
%endif

%if %{?fedora}%{!?fedora:0} >= 16 || %{?rhel}%{!?rhel:0} >= 7
%global with_gcj %{!?_with_gcj:0}%{?_with_gcj:1}
%else
%global with_gcj %{!?_without_gcj:1}%{?_without_gcj:0}
%endif

%global version1 1.9.19.2
%global release1 9

%global version2 2.0.6
%global release2 6

Name:		voms
Version:	%{version2}
Release:	%{release2}%{?dist}
Summary:	Virtual Organization Membership Service

Group:		System Environment/Libraries
License:	ASL 2.0
URL:		http://glite.web.cern.ch/glite/
#		This source tarball is created from a git checkout:
#		git clone git://testbed002.cnaf.infn.it/opt/gits/voms.git
#		cd voms
#		git archive --format tar --prefix voms-2.0.2/ voms_R_2_0_2 | \
#		gzip - > ../voms-2.0.2.tar.gz
Source0:	%{name}-%{version2}.tar.gz
#		This source tarball is created from a CVS checkout:
#		cvs -d:pserver:anonymous:@glite.cvs.cern.ch:/cvs/glite co \
#		  -r glite-security-voms_R_1_9_19_2 \
#		  -d voms-1.9.19.2 org.glite.security.voms
#		tar -z -c --exclude CVS -f voms-1.9.19.2.tar.gz voms-1.9.19.2
Source1:	%{name}-%{version1}.tar.gz
#		Post-install setup instructions:
Source2:	%{name}.INSTALL
#		Build using Globus from Fedora/EPEL
#		https://savannah.cern.ch/bugs/?54427
Source3:        voms.logrotate
Patch0:		%{name}-distribution-globus.patch
#		Fix the start-up script
#		https://savannah.cern.ch/bugs/?54428
Patch1:		%{name}-initscript.patch
#		Fix the --disable-glite configure option
#		https://savannah.cern.ch/bugs/?54429
Patch2:		%{name}-fix-enable-glite.patch
#		Remove lib64 hardcoding
#		https://savannah.cern.ch/bugs/?54430
Patch3:		%{name}-nolib64.patch
#		Make the Java API more compatible with the C API
#		https://savannah.cern.ch/bugs/?54432
Patch4:		%{name}-extra-vomses-java.patch
#		Missing casts after Java cloning
#		https://savannah.cern.ch/bugs/?54433
Patch5:		%{name}-java-clone-cast.patch
#		Fix permissions of installed jar
#		https://savannah.cern.ch/bugs/?54434
Patch6:		%{name}-jar-perms.patch
#		Fix javadoc warnings
#		https://savannah.cern.ch/bugs/?54435
Patch7:		%{name}-javadoc.patch
#		Fix syntax errors in shell scripts
#		https://savannah.cern.ch/bugs/?54436
Patch8:		%{name}-shell-syntax.patch
#		Fix the database install script
#		https://savannah.cern.ch/bugs/?54880
Patch9:		%{name}-install-db.patch
#		Error message glitch
#		https://savannah.cern.ch/bugs/?55113
Patch10:	%{name}-notknown-msg.patch
#		Make the Java API build with gcj
#		https://savannah.cern.ch/bugs/?55115
Patch11:	%{name}-gcj.patch
#		Support older autotools and older gcc
#		https://savannah.cern.ch/bugs/?55116
Patch12:	%{name}-portability.patch
#		Support openssl 1.0
#		https://savannah.cern.ch/bugs/?55390
Patch13:	%{name}-openssl.patch
#		Unconditional use of PIPE_BUF
#		https://savannah.cern.ch/bugs/?55405
Patch14:	%{name}-pipe-buf.patch
#		Make sure -L/usr/lib and -L/usr/lib64 is not used
#		https://savannah.cern.ch/bugs/?57261
Patch15:	%{name}-expat.patch
#		Add missing dependencies for stricter binutils
#		https://savannah.cern.ch/bugs/?60979
Patch16:	%{name}-deps.patch
#		Fix the database install script
Patch20:	%{name}-install-db2.patch
#		Resolve race condition in Makefile documentation rules
Patch21:	%{name}-doc-race.patch
#		Don't use embedded gsoap sources
Patch22:	%{name}-gsoap.patch
#		Work around bug in old autotools (RHEL4)
Patch23:	%{name}-old-autotools.patch
#               Fix duplicate definition of globus_mutex_t
Patch100:       globus_thread_h.patch
Patch101:       p12.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	globus-gssapi-gsi-devel%{?_isa}
BuildRequires:	globus-gss-assist-devel%{?_isa}
BuildRequires:	openssl-devel%{?_isa}
BuildRequires:	expat-devel
BuildRequires:	gsoap-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl
BuildRequires:	doxygen
%if %{?fedora}%{!?fedora:0} >= 9 || %{?rhel}%{!?rhel:0} >= 5
BuildRequires:	tex(latex)
%else
BuildRequires:	tetex-latex
%endif

%if %{withjava}
BuildRequires:	java-devel >= 1:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	bouncycastle >= 1.39
BuildRequires:	jakarta-commons-cli
BuildRequires:	jakarta-commons-lang
BuildRequires:	log4j
%if %{with_gcj}
BuildRequires:	java-gcj-compat-devel
%endif
%endif

%description
In grid computing, and whenever the access to resources may be controlled
by parties external to the resource provider, users may be grouped to
Virtual Organizations (VOs). This package provides a VO Membership Service
(VOMS), which informs on that association between users and their VOs:
groups, roles and capabilities.

This package offers libraries that applications using the VOMS functionality
will bind to.

%package devel
Summary:	Virtual Organization Membership Service Development Files
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	openssl-devel%{?_isa}
Requires:	automake

%description devel
In grid computing, and whenever the access to resources may be controlled
by parties external to the resource provider, users may be grouped to
Virtual Organizations (VOs). This package provides a VO Membership Service
(VOMS), which informs on that association between users and their VOs:
groups, roles and capabilities.

This package offers header files for programming with the VOMS libraries.

%package doc
Summary:	Virtual Organization Membership Service Documentation
Group:		Documentation
%if %{?fedora}%{!?fedora:0} >= 10 || %{?rhel}%{!?rhel:0} >= 6
BuildArch:	noarch
%endif
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for the Virtual Organization Membership Service.

%if %{compat}
%package compat
Version:	%{version1}
Release:	%{release1}%{?dist}
Summary:	Virtual Organization Membership Service
Group:		System Environment/Libraries

%description compat
In grid computing, and whenever the access to resources may be controlled
by parties external to the resource provider, users may be grouped to
Virtual Organizations (VOs). This package provides a VO Membership Service
(VOMS), which informs on that association between users and their VOs:
groups, roles and capabilities.

This package offers libraries that applications using the VOMS functionality
will bind to.
%endif

%package clients
Version:	%{version2}
Release:	%{release2}%{?dist}
Summary:	Virtual Organization Membership Service Clients
Group:		Applications/Internet
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description clients
In grid computing, and whenever the access to resources may be controlled
by parties external to the resource provider, users may be grouped to
Virtual Organizations (VOs). This package provides a VO Membership Service
(VOMS), which informs on that association between users and their VOs:
groups, roles and capabilities.

This package provides command line applications to access the VOMS
services.

%package server
Summary:	Virtual Organization Membership Service Server
Group:		Applications/Internet
Requires:	%{name}%{?_isa} = %{version}-%{release}

Requires(pre):		shadow-utils
Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(postun):	initscripts

%description server
In grid computing, and whenever the access to resources may be controlled
by parties external to the resource provider, users may be grouped to
Virtual Organizations (VOs). This package provides a VO Membership Service
(VOMS), which informs on that association between users and their VOs:
groups, roles and capabilities.

The service can be understood as an account database, which serves the
information in a special format (VOMS credential). The VO manager can
administrate it remotely using command line tools or a web interface.

%if %{withjava}
%package -n vomsjapi
Summary:	Virtual Organization Membership Service Java API
Group:		Development/Libraries
Requires:	java
Requires:	jpackage-utils
Requires:	bouncycastle >= 1.39
Requires:	jakarta-commons-cli
Requires:	jakarta-commons-lang
Requires:	log4j
%if %{with_gcj}
Requires(post):		java-gcj-compat
Requires(postun):	java-gcj-compat
%else
%if %{?fedora}%{!?fedora:0} >= 10
BuildArch:	noarch
%endif
%endif

%description -n vomsjapi
In grid computing, and whenever the access to resources may be controlled
by parties external to the resource provider, users may be grouped to
Virtual Organizations (VOs). This package provides a VO Membership Service
(VOMS), which informs on that association between users and their VOs:
groups, roles and capabilities.

This package offers a java client API for VOMS.

%package -n vomsjapi-javadoc
Summary:	Virtual Organization Membership Service Java API Documentation
Group:		Documentation
%if %{?fedora}%{!?fedora:0} >= 10
BuildArch:	noarch
%endif
Requires:	jpackage-utils
Requires:	vomsjapi = %{version}-%{release}

%description -n vomsjapi-javadoc
Virtual Organization Membership Service (VOMS) Java API Documentation.
%endif

%prep
%if %{compat}
%setup -q -a 1

pushd %{name}-%{version1}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

# Fix bad permissions (which otherwise end up in the debuginfo package)
find . '(' -name '*.h' -o -name '*.c' -o -name '*.cpp' -o \
	   -name '*.cc' -o -name '*.java' ')' -exec chmod a-x {} ';'

# Fix location dir
sed -e 's/\(LOCATION_DIR.*\)"\$prefix"/\1""/g' -i project/acinclude.m4

# Fix default Globus location
sed -e 's!\(GLOBUS_LOCATION\)!{\1:-/usr}!' -i project/voms.m4

# Fix default vomses file location
sed -e 's!/opt/glite/etc/vomses!/etc/vomses!' -i src/api/ccapi/voms_api.cc

# Use pdflatex
sed -e 's!^\(USE_PDFLATEX *= *\)NO!\1YES!' -i src/api/ccapi/Makefile.am

# Touch to avoid rerunning bison and flex
touch -r src/utils/vomsfake.y src/utils/vomsparser.h
touch -r src/utils/vomsfake.y src/utils/vomsparser.c
touch -r src/utils/vomsfake.y src/utils/lex.yy.c

# rebootstrap
./autogen.sh

popd

%else
%setup -q
%endif

%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

# Remove embedded gsoap sources
rm src/server/stdsoap2.c src/server/stdsoap2.h src/server/soap*

# Fix bad permissions (which otherwise end up in the debuginfo package)
find . '(' -name '*.h' -o -name '*.c' -o -name '*.cpp' -o \
	   -name '*.cc' -o -name '*.java' ')' -exec chmod a-x {} ';'

# Use pdflatex
sed -e 's!^\(USE_PDFLATEX *= *\)NO!\1YES!' -i src/api/ccapi/Makefile.am

# Touch to avoid rerunning bison and flex
touch -r src/utils/vomsfake.y src/utils/vomsparser.h
touch -r src/utils/vomsfake.y src/utils/vomsparser.c
touch -r src/utils/vomsfake.y src/utils/lex.yy.c

# rebootstrap
./autogen.sh

install -m 644 %{SOURCE2} README.Fedora

# OSG patches
%patch100 -p1
%patch101 -p1

%build
%if %{compat}
pushd %{name}-%{version1}
%configure --disable-glite --libexecdir=%{_datadir} --sysconfdir=%{_datadir} \
	   --disable-static --disable-docs --disable-java \
	   --with-api-only
make -j1
popd
%endif

%configure --disable-glite --libexecdir=%{_datadir} --sysconfdir=%{_datadir} \
	   --disable-static --enable-docs \
%if %{withjava}
	   --with-java-home=/usr --with-bc=/usr/share/java/bcprov.jar \
	   --with-log4j=/usr/share/java/log4j.jar \
	   --with-commons-cli=/usr/share/java/commons-cli.jar \
	   --with-commons-lang=/usr/share/java/commons-lang.jar
%else
	   --disable-java
%endif

make -j1

( cd doc/apidoc/api/VOMS_C_API/latex ; make )
( cd doc/apidoc/api/VOMS_CC_API/latex ; make )

%if %{withjava}
mkdir javadoc
cd javadoc
CLASSPATH=../src/api/java:$(build-classpath \
			    bcprov log4j commons-cli commons-lang) \
javadoc ../src/api/java/org/glite/voms/*.java \
	../src/api/java/org/glite/voms/ac/*.java \
	../src/api/java/org/glite/voms/contact/*.java
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{compat}
pushd %{name}-%{version1}
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_datadir}
popd
%endif

make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/*.la

rm $RPM_BUILD_ROOT%{_mandir}/man8/voms-install-replica.8*

mv $RPM_BUILD_ROOT%{_datadir}/vomses.template \
   $RPM_BUILD_ROOT%{_datadir}/%{name}

mv $RPM_BUILD_ROOT%{_datadir}/m4 $RPM_BUILD_ROOT%{_datadir}/aclocal

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/vomsdir
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}

# Turn off default enabling of the service
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
sed -e 's/\(chkconfig: \)\w*/\1-/' \
    -e '/Default-Start/d' \
    -e 's/\(Default-Stop:\s*\).*/\10 1 2 3 4 5 6/' \
   $RPM_BUILD_ROOT%{_datadir}/init.d/%{name} > \
   $RPM_BUILD_ROOT%{_initrddir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_initrddir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_datadir}/init.d

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
echo VOMS_USER=voms > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 -p LICENSE AUTHORS $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/VOMS_C_API
cp -pr doc/apidoc/api/VOMS_C_API/html \
   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/VOMS_C_API
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/VOMS_C_API/html/installdox
install -m 644 doc/apidoc/api/VOMS_C_API/latex/refman.pdf \
   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/VOMS_C_API

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/VOMS_CC_API
cp -pr doc/apidoc/api/VOMS_CC_API/html \
   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/VOMS_CC_API
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/VOMS_CC_API/html/installdox
install -m 644 doc/apidoc/api/VOMS_CC_API/latex/refman.pdf \
   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/VOMS_CC_API

%if %{withjava}
mv $RPM_BUILD_ROOT%{_javadir}/vomsjapi.jar \
   $RPM_BUILD_ROOT%{_javadir}/vomsjapi-%{version}.jar
ln -s vomsjapi-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/vomsjapi.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -pr javadoc $RPM_BUILD_ROOT%{_javadocdir}/vomsjapi-%{version}
ln -s vomsjapi-%{version} $RPM_BUILD_ROOT%{_javadocdir}/vomsjapi

%if %{with_gcj}
%{_bindir}/aot-compile-rpm
%endif
%endif

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
cp %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%posttrans
# Recover /etc/vomses...
if [ -r %{_sysconfdir}/vomses.rpmsave -a ! -r %{_sysconfdir}/vomses ] ; then
   mv %{_sysconfdir}/vomses.rpmsave %{_sysconfdir}/vomses
fi

%if %{compat}
%post compat -p /sbin/ldconfig

%postun compat -p /sbin/ldconfig
%endif

%pre server
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} \
    -d %{_sysconfdir}/%{name} -s /sbin/nologin -c "VOMS Server Account" %{name}
exit 0

%post server
if [ $1 = 1 ]; then
    /sbin/chkconfig --add %{name}
fi

%preun server
if [ $1 = 0 ]; then
    /sbin/service %{name} stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}
fi

%postun server
if [ $1 -ge 1 ]; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi

%if %{withjava}
%post -n vomsjapi
%if %{with_gcj}
[ -x %{_bindir}/rebuild-gcj-db ] && %{_bindir}/rebuild-gcj-db
%endif

%postun -n vomsjapi
%if %{with_gcj}
[ -x %{_bindir}/rebuild-gcj-db ] && %{_bindir}/rebuild-gcj-db
%endif
%endif

%files
%defattr(-,root,root,-)
%{_libdir}/libvomsapi.so.1*
%dir %{_sysconfdir}/grid-security
%dir %{_sysconfdir}/grid-security/vomsdir
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/vomses.template
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/AUTHORS
%doc %{_docdir}/%{name}-%{version}/LICENSE

%files devel
%defattr(-,root,root,-)
%{_libdir}/libvomsapi.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}-2.0.pc
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man3/*

%if %{compat}
%files compat
%defattr(-,root,root,-)
%{_libdir}/libvoms*.so.0*
%doc %{name}-%{version1}/AUTHORS
%doc %{name}-%{version1}/LICENSE
%endif

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}/VOMS_C_API
%doc %{_docdir}/%{name}-%{version}/VOMS_CC_API

%files clients
%defattr(-,root,root,-)
%{_bindir}/voms-proxy-destroy
%{_bindir}/voms-proxy-info
%{_bindir}/voms-proxy-init
%{_bindir}/voms-proxy-fake
%{_bindir}/voms-proxy-list
%{_mandir}/man1/voms-proxy-destroy.1*
%{_mandir}/man1/voms-proxy-info.1*
%{_mandir}/man1/voms-proxy-init.1*
%{_mandir}/man1/voms-proxy-fake.1*
%{_mandir}/man1/voms-proxy-list.1*

%files server
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/grid-security/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(-,voms,voms) %dir %{_localstatedir}/log/%{name}
%{_datadir}/%{name}/mysql2oracle
%{_datadir}/%{name}/upgrade1to2
%{_datadir}/%{name}/voms.data
%{_datadir}/%{name}/voms_install_db
%{_datadir}/%{name}/voms-ping
%{_datadir}/%{name}/voms_replica_master_setup.sh
%{_datadir}/%{name}/voms_replica_slave_setup.sh
%{_mandir}/man8/voms.8*
%doc README.Fedora

%if %{withjava}
%files -n vomsjapi
%defattr(-,root,root,-)
%{_javadir}/vomsjapi.jar
%{_javadir}/vomsjapi-%{version}.jar
%if %{with_gcj}
%{_libdir}/gcj/%{name}
%endif
%doc AUTHORS LICENSE

%files -n vomsjapi-javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/vomsjapi
%doc %{_javadocdir}/vomsjapi-%{version}
%endif

%changelog
* Thu May 24 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 2.0.6-6
- Add logrotate file

* Sun Nov 5 2011 Alain Roy <roy@cs.wisc.edu> - 2.0.6-5
- Added bug fix so misstyped passphrase when using p12 file doesn't cause segfault. 

* Fri Oct 28 2011 Matyas Selmeci <matyas@cs.wisc.edu> - 2.0.6-4
- Rebuilt

* Thu Sep 29 2011 Matyas Selmeci <matyas@cs.wisc.edu> - 2.0.6-3
- Release bump of voms and voms-compat

* Wed Sep 28 2011 Derek Weitzel <dweitzel@cse.unl.edu> - 2.0.6-2
- Updated to 2.0.6 
- Changed compat to include *.0

* Mon Sep 12 2011 Matyas Selmeci <matyas@cs.wisc.edu> - 2.0.2-3
- Rebuild against updated Globus libraries
- also bumped voms-compat revision to 5
- removed parallel make

* Fri May 27 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.2-1
- Update to version 2.0.2
- Add compat package for older releases
- Drop Java AOT compilation for newer releases

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 26 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.19.2-2
- Make vomsjapi-javadoc arch depenent on EPEL

* Mon Nov 01 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.19.2-1
- Upstream 1.9.19.2 (CVS tag glite-security-voms_R_1_9_19_2)

* Sun Oct 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.18.1-3
- Add posttrans scriptlet to recover /etc/vomses

* Fri Oct 15 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.18.1-2
- Remove the empty /etc/vomses file - it will cause conflicts for users
  that have used the option to have /etc/vomses be a directory

* Mon Oct 04 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.18.1-1
- Upstream 1.9.18.1 (CVS tag glite-security-voms_R_1_9_18_1)

* Thu Jul 08 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.17.1-2
- Make -doc subpackage depend of main package for license reasons

* Sat Jun 05 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.17.1-1
- Upstream 1.9.17.1 (CVS tag glite-security-voms_R_1_9_17_1)
- Drop patches voms-db-method.patch and voms-thread.patch (accepted upstream)

* Sat Apr 03 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.16.1-2.1
- Enable java for x86 and x86_64

* Sun Mar 28 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.16.1-2
- Add mutex lock for accessing private data

* Fri Mar 19 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.16.1-1
- Upstream 1.9.16.1 (CVS tag glite-security-voms_R_1_9_16_1)
- Fix uninitialized variable in voms-proxy-init

* Mon Dec 28 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.14.3-1
- Upstream 1.9.14.3 (CVS tag glite-security-voms_R_1_9_14_3)
- Add missing dependencies for stricter binutils

* Tue Oct 20 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.14.2-1
- Upstream 1.9.14.2 (CVS tag glite-security-voms_R_1_9_14_2)

* Fri Sep 18 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.12.1-1
- Upstream 1.9.12.1 (CVS tag glite-security-voms_R_1_9_12_1)

* Mon Sep 07 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.11-4
- Fix building with openssl 1.0

* Thu Sep 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.11-3
- Add an empty /etc/vomses file to the main package to avoid error messages
- Let the voms user own only necessary directories
- Additional fixes for the server start-up script

* Tue Aug 25 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.11-2
- Add the /etc/voms directory to the server package
- Add setup instructions to the server package
- Run the server as non-root

* Fri Aug 14 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.11-1
- Upstream 1.9.11 (CVS tag glite-security-voms_R_1_9_11)
- Enable Java AOT bits

* Mon Jun 29 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.8.1-1
- Upstream 1.9.8.1 (CVS tag glite-security-voms_R_1_9_8_1)
- Build Java API

* Thu Feb 12 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.2-1
- Upstream 1.9.2 (CVS tag glite-security-voms_R_1_9_2)

* Fri Feb 06 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.1-1
- Upstream 1.9.1 (CVS tag glite-security-voms_R_1_9_1)

* Tue Jan 06 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.8.10-1
- Upstream 1.8.10 (CVS tag glite-security-voms_R_1_8_10)
- Rebuild against distribution Globus
- Add clear SSL error patch needed for openssl > 0.9.8b
- Add missing return value patch

* Sun Oct 26 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.8.9-1ng
- Upstream 1.8.9 (CVS tag glite-security-voms_R_1_8_9)
- Rebuild against Globus 4.0.8-0.11

* Thu May 15 2008 Anders Wäänänen <waananen@nbi.dk> - 1.7.24-4ng
- Add missing include patch

* Sat Apr 26 2008 Anders Wäänänen <waananen@nbi.dk> - 1.7.24-3ng
- Rebuild against Globus 4.0.7-0.10

* Sun Nov 25 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.24-2ng
- Fix GPT_LOCATION and GLOBUS_LOCATION detection in spec file

* Mon Oct 29 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.24-1ng
- Upstream 1.7.24 (CVS tag glite-security-voms_R_1_7_24_1)

* Mon Oct 15 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.23-1ng
- Upstream 1.7.23 (CVS tag glite-security-voms_R_1_7_23_1)

* Wed Sep 12 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.22-3ng
- Move /etc/voms/vomses back to /etc/vomses
- Added more openssl portability patches with input
  from Aake Sandgren <ake.sandgren@hpc2n.umu.se>

* Wed Sep 12 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.22-2ng
- Added more openssl portability patches with input
  from Aake Sandgren <ake.sandgren@hpc2n.umu.se>

* Mon Sep 10 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.22-1ng
- Try to link against system crypto library when Globus library is not
  available
- Make /etc/grid-security/vomsdir part of the voms sub-package
- Drop RPM prefix /etc
- Move the vomses.template to /etc/voms
- Use dashes instead of underscore in voms-install-replica.1 man page
- Do not try to link against system crypt library. Voms now
  does this internally.
- Upstream 1.7.22 (CVS tag glite-security-voms_R_1_7_22_1)

* Mon Jul 16 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.20-5ng
- Drop voms-struct_change.patch - problem is with libxml2

* Sat Jul 14 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.20-4ng
- Add missing openssl-devel dependency in voms-devel

* Thu Jul 12 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.20-3ng
- Add patch:
  - voms-struct_change.patch
    - Change API slightly - but now works with libxml2

* Thu Jul 08 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.20-2ng
- Make conditinal dependency on expat-devel (OpenSuSE 10.20 has only expat)

* Thu Jul 05 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.20-1ng
- Upstream 1.7.20 (CVS tag glite-security-voms_R_1_7_20_1) 

* Thu Jul 05 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.19-2ng
- Added patches:
  - voms-openssl_portability.patch
    - Support for newer OpenSSL-0.9.8
  - voms-isoc90_portability.patch
    - Support for older compilers
- Added openssl-devel build dependency

* Fri Jun 22 2007 Anders Wäänänen <waananen@nbi.dk> - 1.7.19-1ng
- Upstream 1.7.19 (CVS tag glite-security-voms_R_1_7_19_P2) 
- Remove patches (use shell substitutions instead)
- Disable Java API build

* Fri Jun 22 2007 Anders Wäänänen <waananen@nbi.dk> - 1.6.20-3ng
- Added Globus dependencies to voms-devel

* Mon Jul 24 2006 Anders Wäänänen <waananen@nbi.dk> - 1.6.20-2ng
- Fix dependency typo: Requires -> BuildRequires

* Sat May 06 2006 Anders Wäänänen <waananen@nbi.dk> - 1.6.20-1ng
- Many changes since upstream changed quite a lot.
- Added README.NorduGrid with packaging information
- Patches:
  - voms_openssl-0.9.8.patch
    - Support for OpenSSL 0.9.8
  - voms_noglobusopenssl-1.6.20.patch
    - Use system openssl rather than the one from Globus
    - Patch reworked for voms 1.6.20
  - Dont use project based (gLite) include paths
- Pseudo patches (fixes made at runtime and not from static patch files)
  - Fix broken --libexecdir support for configure
    (some systems do not have libexecdir = <prefix>/libexec)
  - Drop all documents except man pages which are pre-generated
    (section 3 man pages are skipped as well)
  - Do not use edg- prefix
    (can be turned on/off through macro)
  - Install flavored libraries in addition to non-flavored
    (can be turned on/off through macro)
  - Put start-up script in /etc/init.d
  - Move configuration files from <prefix>/etc to /etc

* Mon Dec 19 2005 Anders Wäänänen <waananen@nbi.dk> - 1.6.9-2
- Add patch voms_doc.patch to disable html and ps documentation
  and add man-mages and pdf files to distribution (make dist)
- Use rpm switch: --define "_autotools_bootstrap 1" to rebuild
  documentation and create "make dist" target
- Add patch voms_nohardcodelibexecdir.patch which use the libexecdir
  from configure rather than the hardcoded prefix/libexec

* Sun Nov 27 2005 Anders Wäänänen <waananen@nbi.dk> - 1.6.9-1
- Add patch voms_ssl_include.patch to add external openssl includes.
  Would be better to query globus_openssl about this

* Tue Oct 18 2005 Anders Wäänänen <waananen@nbi.dk> - 1.6.7-1
- Modfiy voms_noglobusopenssl.patch to match upstream
- Add patch voms_nops.patch to disable postscript versions of
  reference manual

* Fri Jun 17 2005 Anders Wäänänen <waananen@nbi.dk> - 1.5.4-1
- Remove the following patches:
  - voms_namespace.patch - Fixed in upstream
  - voms_external_mysql++-1.4.1.patch - Obsolete since mysql++ is no
    longer needed
  - voms-no_libs.path - Fixed in upstream
- Add Globus dependencies

* Wed Jun 01 2005 Anders Wäänänen <waananen@nbi.dk> - 1.4.1-3
- Do not hardcode Globus flavor but try to guess
- Remove explicit globus rpm Requirement
- Use external openssl - not globus_openssl

* Mon May 02 2005 Anders Wäänänen <waananen@nbi.dk> - 1.4.1-2
- Remove automake cache
- Add explicit dependency on mysql++-devel

* Sat Apr 30 2005 Anders Wäänänen <waananen@nbi.dk> - 1.4.1-1
- New upstream
- autogen.sh -> autobuild.sh

* Mon Apr 18 2005 Anders Wäänänen <waananen@nbi.dk> - 1.3.2-1
- Initial build.
