## Turn off meaningless jar repackaging 
%define __jar_repack 0

# If set, the maven build is done in offline mode and a tarball of the maven
# dependencies (basically the local repository tarred up) is used.
%define maven_offline 0

Summary: The VOMS Administration service
Name: voms-admin-server
Version: 2.7.0
Release: 1.22%{?dist}
License: ASL 2.0
Group: System Environment/Libraries

%if %{?rhel} < 7

BuildRequires:  maven22
BuildRequires:  jpackage-utils
BuildRequires:  java7-devel
%define mvn mvn22

%else

BuildRequires:  maven >= 3.0
%define mvn mvn

%endif

%if 0%{?maven_offline}
%define mvnopts -B -o
%else
%define mvnopts -B
%endif

BuildRequires:  emi-trustmanager
BuildRequires:  emi-trustmanager-axis
BuildRequires:  /usr/share/java/jta.jar

Requires: jpackage-utils
Requires: java7-devel
Requires: emi-trustmanager
Requires: emi-trustmanager-tomcat
Requires: bouncycastle >= 1.39

%if 0%{?rhel} <= 5
Requires: tomcat5
Requires: fetch-crl3
%define tomcat tomcat5
%define tomcat_lib /usr/share/tomcat5/common/lib
%define tomcat_endorsed /usr/share/tomcat5/common/endorsed
%define catalina_home /usr/share/tomcat5
%endif

%if 0%{?rhel} == 6
Requires: tomcat6
Requires: fetch-crl
%define tomcat tomcat6
%define tomcat_lib /usr/share/tomcat6/lib
%define tomcat_endorsed /usr/share/tomcat6/endorsed
%define catalina_home /usr/share/tomcat6
%endif

%if 0%{?rhel} >= 7
Requires: tomcat
Requires: fetch-crl
%define tomcat tomcat
%define tomcat_lib /usr/share/%tomcat/lib
%define tomcat_endorsed /usr/share/%tomcat/endorsed
%define catalina_home /usr/share/%tomcat
%endif

Requires(post):/sbin/chkconfig
Requires(preun):/sbin/chkconfig
Requires(preun):/sbin/service
Requires(postun):/sbin/service
# The following requirement makes sure we get the RPM that provides this,
# and not just the JDK which happens to provide it, but not in the right spot. 
# Requires: xml-commons-apis
Requires: /usr/share/java/xml-commons-apis.jar
Requires: grid-certificates >= 7
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
AutoReqProv: yes
Source0:  %{name}-%{version}.tar.gz

%if 0%{?maven_offline}

Source6:     voms-admin-server-mvn-deps-el6.tar.gz
Source7:     voms-admin-server-mvn-deps-el7.tar.gz

    %if 0%{?el6}
        %define mvn_deps_tarball %{SOURCE6}
    %endif

    %if 0%{?el7}
        %define mvn_deps_tarball %{SOURCE7}
    %endif

%endif


Patch1: 0001-directory-defaults.patch
Patch2: 0002-maven-resources-disable.patch
Patch3: 0003-cern-mirror-disable.patch
Patch4: 0004-trustmanager-versions.patch
Patch5: 0005-fix-suspended-users.patch
Patch6: 0006-fix-certificate-issuer-check.patch
Patch7: 0007-axistools-version.patch
Patch8: 0008-sign-on-behalf-of.patch
Patch9: 0009-disable-ca-check.patch
Patch10: 0010-bump-struts-version-to-2.3.32-SOFTWARE-2652.patch
Patch11: 0011-Fix-RegexFieldValidator-for-Struts-2.3.32.patch
Patch12: 0012-getUri-is-now-in-RequestUtils-SOFTWARE-2652.patch
Patch13: 0013-hibernate-version-4.2.8-drop-hibernate-annotations-S.patch
Patch14: 0014-port-non-whitespace-changes-to-struts.xml-from-88f50.patch
Patch15: 0015-excludeParams-changes-to-struts.xml-from-023f48442-S.patch
Patch16: 0016-enable.DynamicMethodInvocation-true-SOFTWARE-2652.patch
Patch17: 0017-RoleActionSupport.java-changes-from-03e6041f-SOFTWAR.patch
Patch18: 0018-Port-changes-from-01064e71f-SOFTWARE-2652.patch
Patch19: 0019-try-to-work-around-unreported-exception-build-error-.patch
Patch20: 0020-pull-in-.hbm.xml-changes-from-03e6041ff-SOFTWARE-265.patch
Patch21: 0021-bump-c3p0-version-to-0.9.5.2-per-01064e71f-03e6041ff.patch
Patch22: 0022-Use-legacy-naming-strategy.patch
Patch23: 0023-Fix-Hibernate-and-Struts-DTD-namespaces.patch
Patch24: 0024-Add-attribute-annotations-from-9467dda.patch
Patch25: 0025-Drop-PrefixBasedActionMapper-and-pull-some-changes-f.patch
Patch26: 0026-Id-JoinColumn-PrimaryKeyJoinColumn.patch
Patch27: 0027-Assign-CreateAction-to-user-creation-form.patch
Patch28: 0028-Accept-action-param-with-dashes.patch
Patch29: 0029-Re-enable-bulk-suspend-and-membership-extension.patch
Patch30: 0030-Fix-DB-deployment-issues-with-admin-table.patch
Patch31: 0031-Avoid-duplicate-javassist-jars-from-c4d06fe7.patch

Requires: osg-webapp-common

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

The VOMS Admin service is a web application providing tools for administering
the VOMS VO structure. It provides an intuitive web user interface for daily
administration tasks.

%prep


%setup -q -n voms-admin
%patch1 -p0
%if 0%{?rhel} >= 6
# Tried to "BuildRequires: maven-resources-plugin" like in voms-admin-client,
# but it gave me an odd NoClassDefFoundError
# so I'm using a patch to disable using the maven-resources-plugin for el6
# instead. It's just used for copying two spec files that we neither use, nor
# include in the final package. -mat
%patch2 -p0
%endif
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0

%if 0%{?rhel} >= 7
%patch7 -p1
%endif

%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1

%define local_maven /tmp/m2/repository


%build

# If we're using maven in offline mode, then copy our maven dependencies from
# the tarball(s) we have into the local mvn repo
%if 0%{?maven_offline}

    rm -rf "%{local_maven}"
    # Do not copy over these deps into the local repo because we already have
    # them by other means
    DEP_BLACKLIST=(
                   emi/trustmanager
                   emi/trustmanager-axis
                   javax/transaction
                  )

    tar -xzf "%{mvn_deps_tarball}"

    (
        cd repository
        for dep in "${DEP_BLACKLIST[@]}"; do
            rm -rf "$dep"
        done
        mkdir -p "%{local_maven}"
        mv -f * "%{local_maven}/"
    )
    rm -rf repository

%endif

# Fix tomcat directory location in init script
# The directory-defaults.patch adds the line we're fixing here
sed -i -e 's/@TOMCAT@/%{tomcat}/' resources/scripts/init-voms-admin.py

mvn_install_file () {
    groupId=$1
    artifactId=$2
    version=$3
    file=$4

    # Get out of the package dir so maven won't look at the package's pom.xml
    pushd /tmp

    %mvn %mvnopts install:install-file \
        -DgroupId="$groupId" \
        -DartifactId="$artifactId" \
        -Dversion="$version" \
        -Dpackaging=jar \
        -Dfile="$file" \
        -Dmaven.repo.local="%{local_maven}"
    popd
}

# Adding system dependencies
mvn_install_file  emi trustmanager 3.0.3 "`build-classpath trustmanager`"
mvn_install_file  emi trustmanager-axis 1.0.1 "`build-classpath trustmanager-axis`"
mvn_install_file  javax.transaction jta 1.0.1B "`build-classpath jta`"

export JAVA_HOME=%{java_home};
%mvn %mvnopts -s src/config/emi-build-settings.xml -e -P EMI -Dmaven.repo.local="%{local_maven}" package



%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
tar xzvf target/%{name}-%{version}.tar.gz -C $RPM_BUILD_ROOT
# Fix some randomly broken permissions
chmod 644 $RPM_BUILD_ROOT/usr/share/webapps/glite-security-voms-siblings.war $RPM_BUILD_ROOT/usr/share/webapps/glite-security-voms-admin.war $RPM_BUILD_ROOT/usr/share/java/glite-security-voms-admin.jar $RPM_BUILD_ROOT/usr/share/voms-admin/tools/classes/logback.xml $RPM_BUILD_ROOT/usr/share/voms-admin/tools/classes/c3p0.properties 
chmod 755 $RPM_BUILD_ROOT/usr/sbin/voms.py $RPM_BUILD_ROOT/usr/sbin/voms-admin-configure $RPM_BUILD_ROOT/etc/rc.d/init.d/voms-admin
# Fix sysconfig file
sed -i -e 's|^CATALINA_HOME=.*|CATALINA_HOME=%{catalina_home}|' $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/voms-admin
## Stage oracle jar
#cp `find /usr/lib/oracle/ -name ojdbc14.jar` $RPM_BUILD_ROOT%{_datadir}/voms-admin/tools/lib
find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
find $RPM_BUILD_ROOT -name '*.pc' -exec sed -i -e "s|$RPM_BUILD_ROOT||g" {} \;

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/voms-admin

mkdir -p $RPM_BUILD_ROOT%{tomcat_lib}
ln -s /usr/share/java/eclipse-ecj.jar $RPM_BUILD_ROOT%{tomcat_lib}/voms-admin-eclipse-ecj.jar

mkdir -p $RPM_BUILD_ROOT%{tomcat_endorsed}/
ln -s /usr/share/java/xalan-j2.jar $RPM_BUILD_ROOT%{tomcat_endorsed}/
ln -s /usr/share/java/xalan-j2-serializer.jar $RPM_BUILD_ROOT%{tomcat_endorsed}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add voms-admin

%preun
if [ $1 = 0 ]; then
    /sbin/service voms-admin stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del voms-admin
fi



%files
%defattr(-,root,root)
%attr(-,tomcat,tomcat) %dir %{_sysconfdir}/voms-admin
%{_initrddir}/voms-admin
%dir %{_datadir}/webapps/
%{_datadir}/webapps/glite-security-voms-siblings.war
%{_datadir}/webapps/glite-security-voms-admin.war
%{_javadir}/glite-security-voms-admin.jar
%config(noreplace) %{_sysconfdir}/sysconfig/voms-admin
%docdir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}/AUTHORS
%{_datadir}/doc/%{name}-%{version}/README
%{_datadir}/doc/%{name}-%{version}/license.txt
%{_datadir}/doc/%{name}-%{version}/NEWS

%{_sbindir}/*
%{_datadir}/voms-admin/*
%{tomcat_lib}/voms-admin-eclipse-ecj.jar
%{tomcat_endorsed}/xalan-j2.jar
%{tomcat_endorsed}/xalan-j2-serializer.jar

%changelog
* Thu May 18 2017 Brian Lin <blin@cs.wisc.edu> - 2.7.0-1.22
- Release voms-admin-server-2.7.0-1.22+ (SOFTWARE-2652)

* Tue Jan 26 2016 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.21
- Port VOMS-678 fix for broken user lookup by subject (SOFTWARE-2158)

* Thu Jan 14 2016 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.19
- Port VOMS-605 option to skip CA check (SOFTWARE-2158)

* Fri Oct 30 2015 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.17
- Restore 'Sign AUP on behalf of user' feature (SOFTWARE-2091)

* Thu Aug 06 2015 Mátyás Selmeci <matyas@cs.wisc.edu> 2.7.0-1.16.osg
- Build for el6 and el7; optionally use a bundle of mvn dependencies so we can build in offline mode

* Tue Jul 21 2015 Mátyás Selmeci <matyas@cs.wisc.edu> 2.7.0-1.15.osg
- Changes to build on el7 with tomcat 7

* Wed Jul 01 2015 Mátyás Selmeci <matyas@cs.wisc.edu> - 2.7.0-1.14
- Require grid-certificates >= 7 (SOFTWARE-1883)

* Fri May 01 2015 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.13
- drop glite-security-util-java requirement (SOFTWARE-1880)

* Tue Apr 15 2014 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.12
- Do not return expired or suspended users or certificates with
  getGridmapUsers from VOMSCompatibility interface (SOFTWARE-1349)

* Wed Mar 12 2014 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.11
- Require glite-security-util-java (SOFTWARE-1408)
- Remove requirement for xml-commons-apis (covered by explicit jar name)

* Mon Mar 03 2014 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.9
- bump to rebuild against classworlds from jpackage repo (SOFTWARE-1279)

* Thu Feb 27 2014 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.7
- apply patch to fix check for adding new certificates (SOFTWARE-1408)

* Tue Feb 04 2014 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.6
- fix build for voms-admin-server (SOFTWARE-1299)
  - disable cern mirror, fix trustmanager versions, explicitly build require
    /usr/share/java/jta.jar, and add maven dependencies to local maven repo
- apply patch to fix suspended/expired users (SOFTWARE-1349)

* Thu Apr 04 2013 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.5
- Rebuild for updated build dependency

* Tue Feb 26 2013 Carl Edquist <edquist@cs.wisc.edu> - 2.7.0-1.4
- Updates to build with OpenJDK 7; require java7-devel + jpackage-utils

* Fri Feb 22 2013 Brian Lin <blin@cs.wisc.edu> - 2.7.0-1.3
- Update rhel5 to require fetch-crl3 instead of fetch-crl.

* Tue Aug 28 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 2.7.0-1.2
Add symlinks for xalan-j2 to tomcat endorsed dir
Fix CATALINA_HOME in sysconfig file

* Tue Aug 14 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 2.7.0-1.1
Version update; added changes from upstream spec file; its changelog:
  * Fri Dec 16 2011 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 2.7.0-1
  - Self-managed packaging
Removed fix for maven-surefire-plugin on el6--no longer needed
Removed maven-deps patch

* Fri May 25 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 2.6.1-12
Add dependency on osg-webapp-common

* Wed Mar 21 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 2.6.1-11
Make directory-defaults.patch work for tomcat6 as well

* Mon Mar 19 2012 Matyas Selmeci <matyas@cs.wisc.edu> - 2.6.1-10
Fix maven-surefire-plugin on el6
Disable maven-resources-plugin on el6
Fix JAVA_HOME on el6
Use tomcat6 on el6

* Wed Sep 21 2011 Alain Roy <roy@cs.wisc.edu> - 2.6.1-9
Tweaked xml-commons-apis dependency to work
Added chkconfig

* Mon Jul 25 2011 Tanya Levshina <tlevshin@fnal.gov> - 2.6.1-8
changed patch1 - patches voms.py and not voms-admin-configure.py

* Fri Jul 22 2011 Tanya Levshina <tlevshin@fnal.gov> - 2.6.1-7
added requires grid-certificates

* Fri Jul 22 2011 Tanya Levshina <tlevshin@fnal.gov> - 2.6.1-6
added requires xmi-commons-api

* Thu Jul 21 2011 Tanya Levshina <tlevshin@fnal.gov> - 2.6.1-5
added requires (java-sun,fetch-crl), buildrequires (java-sun-devel)

* Thu Jul 21 2011 Tanya Levshina <tlevshin@fnal.gov> - 2.6.1-4
mock creates *.pyc, *.pyo files, so they should be in file

* Thu Jul 21 2011 Tanya Levshina <tlevshin@fnal.gov> - 2.6.1-3
Modified patch, get rid of *.pyc, *.pyo files

 
