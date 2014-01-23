%ifarch i386
%global __os_install_post %{nil}
%global __spec_install_post %{nil}
%global __debug_install_post %{nil}
%global debug_package %{nil}
%undefine __debug_package
%undefine _enable_debug_packages
Name: jdk
Epoch: 2000
Version: 1.6.0_45
Release: fcs.1%{?dist}
Group: Development/Tools
URL: http://www.oracle.com/technetwork/java/javase/overview/index.html
License: Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved. Also under other license(s) as shown at the Description field.
Summary: Java(TM) Platform Standard Edition Development Kit
Source0: jdk-6u45-linux-i586.bin.tar.gz
Source1: jdk-6u45-linux-amd64.bin.tar.gz
AutoReqProv: no
Prefix: /usr/java
Requires: /bin/basename
Requires: /bin/cat
Requires: /bin/cp
Requires: /bin/gawk
Requires: /bin/grep
Requires: /bin/ln
Requires: /bin/ls
Requires: /bin/mkdir
Requires: /bin/mv
Requires: /bin/pwd
Requires: /bin/rm
Requires: /bin/sed
Requires: /bin/sort
Requires: /bin/touch
Requires: /usr/bin/cut
Requires: /usr/bin/dirname
Requires: /usr/bin/expr
Requires: /usr/bin/find
Requires: /usr/bin/tail
Requires: /usr/bin/tr
Requires: /usr/bin/wc
Requires: /bin/sh
Requires: /bin/sh
Requires: /bin/sh
Requires: /bin/sh
Requires: rpmlib(PayloadFilesHavePrefix)
Requires: rpmlib(CompressedFileNames)
Provides: jaxp_parser_impl
Provides: xml-commons-apis
Provides: jdk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
The Java Platform Standard Edition Development Kit (JDK) includes both
the runtime environment (Java virtual machine, the Java platform classes
and supporting files) and development tools (compilers, debuggers,
tool libraries and other tools).

The JDK is a development environment for building applications, applets
and components that can be deployed with the Java Platform Standard
Edition Runtime Environment.



%prep
%setup -n jdk-6u45-linux-i586.extract -T -b 0



%build
exit 0



%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mv * $RPM_BUILD_ROOT
pushd $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/i386/client/classes.jsa)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/i386/client/classes.jsa
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/plugin.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/plugin.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/ext/localedata.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/ext/localedata.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/javaws.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/javaws.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/jsse.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/jsse.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/lib/tools.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/lib/tools.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/deploy.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/deploy.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/charsets.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/charsets.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/rt.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/rt.jar

popd


%files
%defattr(-,root,root,-)
%dir %verify(group md5 size link mtime user mode rdev) /etc/.java
%dir %verify(group md5 size link mtime user mode rdev) /etc/.java/.systemPrefs
%config(noreplace) %verify(group link user mode rdev) /etc/.java/.systemPrefs/.system.lock
%config(noreplace) %verify(group link user mode rdev) /etc/.java/.systemPrefs/.systemRootModFile
%attr(0755,root,root) %config() %verify(group link user mode rdev) /etc/init.d/jexec
%dir %verify(group md5 size link mtime user mode rdev) /usr/java
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/COPYRIGHT
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/LICENSE
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/README.html
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/THIRDPARTYLICENSEREADME.txt
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/ControlPanel
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/HtmlConverter
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/appletviewer
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/apt
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/extcheck
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/idlj
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jar
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jarsigner
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/java
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/java-rmi.cgi
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javac
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javadoc
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javah
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javap
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javaws
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jconsole
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jcontrol
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jdb
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jhat
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jinfo
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jmap
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jps
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jrunscript
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jsadebugd
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jstack
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jstat
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jstatd
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jvisualvm
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/keytool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/native2ascii
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/orbd
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/pack200
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/policytool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/rmic
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/rmid
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/rmiregistry
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/schemagen
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/serialver
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/servertool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/tnameserv
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/unpack200
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/wsgen
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/wsimport
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/xjc
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/classfile_constants.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/jawt.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/jdwpTransport.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/jni.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/jvmti.h
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/linux
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/linux/jawt_md.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/linux/jni_md.h
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/COPYRIGHT
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/LICENSE
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/README
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/THIRDPARTYLICENSEREADME.txt
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/Welcome.html
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/ControlPanel
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/java
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/java_vm
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/javaws
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/jcontrol
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/keytool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/orbd
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/pack200
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/policytool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/rmid
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/rmiregistry
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/servertool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/tnameserv
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/unpack200
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/javaws
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/javaws/javaws
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/alt-rt.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/alt-string.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/applet
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/audio
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/audio/soundbank.gm
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/calendars.properties
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/charsets.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/charsets.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/classlist
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/CIEXYZ.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/GRAY.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/LINEAR_RGB.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/PYCC.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/sRGB.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/content-types.properties
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/ffjcext.zip
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/java-icon.ico
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_de.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_es.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_fr.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_it.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_ja.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_ko.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_pt_BR.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_sv.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_zh_CN.properties
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_zh_HK.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_zh_TW.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/splash.gif
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/applications
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/applications/sun-java.desktop
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/applications/sun-javaws.desktop
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/applications/sun_java.desktop
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/mime
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/mime/packages
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/mime/packages/x-java-archive.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/mime/packages/x-java-jnlp-file.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/dnsns.jar
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/localedata.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/localedata.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/meta-index
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/sunjce_provider.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/sunpkcs11.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/flavormap.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.2.1.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.2.1.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.3.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.3.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.4.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.4.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.6.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.6.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.SuSE.11.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.SuSE.11.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.SuSE.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.SuSE.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Sun.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Sun.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Turbo.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Turbo.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Ubuntu.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Ubuntu.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.properties.src
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaBrightDemiBold.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaBrightDemiItalic.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaBrightItalic.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaBrightRegular.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaSansDemiBold.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaSansRegular.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaTypewriterBold.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaTypewriterRegular.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/fonts.dir
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/client
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/client/Xusage.txt
%attr(0444,root,root) %ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/client/classes.jsa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/client/libjsig.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/client/libjvm.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/headless
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/headless/libmawt.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/jli
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/jli/libjli.so
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/jvm.cfg
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libJdbcOdbc.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libattach.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libawt.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libcmm.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libdcpr.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libdeploy.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libdt_socket.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libfontmanager.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libhprof.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libinstrument.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libioser12.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libj2gss.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libj2pcsc.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libj2pkcs11.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjaas_unix.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjava.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjava_crw_demo.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjavaplugin_jni.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjavaplugin_nscp.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjavaplugin_nscp_gcc29.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjawt.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjdwp.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjpeg.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjsig.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjsound.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libjsoundalsa.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libmanagement.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libmlib_image.so
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libnative_chmod.so
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libnative_chmod_g.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libnet.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libnio.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libnpjp2.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libnpt.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/librmi.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libsaproc.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libsplashscreen.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libunpack.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libverify.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/libzip.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/motif21
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/motif21/libmawt.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/native_threads
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/native_threads/libhpi.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/server
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/server/Xusage.txt
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/server/libjsig.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/server/libjvm.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/xawt
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/i386/xawt/libmawt.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/im
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/im/indicim.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/im/thaiim.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/cursors.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/invalid32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_CopyDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_CopyNoDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_LinkDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_LinkNoDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_MoveDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_MoveNoDrop32x32.gif
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons/sun-java_HighContrast.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons/sun-java_HighContrastInverse.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons/sun-java_LowContrast.png
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/javaws.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/javaws.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jce.jar
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jexec
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jsse.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jsse.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jvm.hprof.txt
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/de
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/de/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/de/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/es
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/es/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/es/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/fr
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/fr/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/fr/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/it
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/it/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/it/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ja
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ja/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ja/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko.UTF-8
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko.UTF-8/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko.UTF-8/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/sv
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/sv/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/sv/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh.GBK
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh.GBK/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh.GBK/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_HK.BIG5HK
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_HK.BIG5HK/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_HK.BIG5HK/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW.BIG5
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW.BIG5/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW.BIG5/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW/LC_MESSAGES/sunw_java_plugin.mo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/logging.properties
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management-agent.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management/jmxremote.access
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management/jmxremote.password.template
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management/management.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management/snmp.acl.template
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/meta-index
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/net.properties
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/LucidaSansDemiOblique.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/LucidaSansOblique.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/LucidaTypewriterBoldOblique.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/LucidaTypewriterOblique.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/fonts.dir
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/plugin.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/plugin.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/psfont.properties.ja
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/psfontj2d.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/resources.jar
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/rt.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/rt.pack
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/US_export_policy.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/blacklist
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/cacerts
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/java.policy
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/java.security
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/javaws.policy
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/local_policy.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/trusted.libraries
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/servicetag
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/servicetag/jdk_header.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/sound.properties
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Abidjan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Accra
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Addis_Ababa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Algiers
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Asmara
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Bamako
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Bangui
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Banjul
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Bissau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Blantyre
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Brazzaville
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Bujumbura
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Cairo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Casablanca
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Ceuta
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Conakry
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Dakar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Dar_es_Salaam
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Djibouti
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Douala
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/El_Aaiun
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Freetown
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Gaborone
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Harare
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Johannesburg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Juba
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Kampala
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Khartoum
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Kigali
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Kinshasa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Lagos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Libreville
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Lome
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Luanda
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Lubumbashi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Lusaka
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Malabo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Maputo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Maseru
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Mbabane
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Mogadishu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Monrovia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Nairobi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Ndjamena
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Niamey
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Nouakchott
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Ouagadougou
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Porto-Novo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Sao_Tome
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Tripoli
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Tunis
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Windhoek
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Adak
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Anchorage
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Anguilla
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Antigua
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Araguaina
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Buenos_Aires
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Catamarca
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Cordoba
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Jujuy
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/La_Rioja
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Mendoza
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Rio_Gallegos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Salta
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/San_Juan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/San_Luis
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Tucuman
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Ushuaia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Aruba
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Asuncion
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Atikokan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Bahia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Bahia_Banderas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Barbados
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Belem
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Belize
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Blanc-Sablon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Boa_Vista
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Bogota
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Boise
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cambridge_Bay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Campo_Grande
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cancun
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Caracas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cayenne
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cayman
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Chicago
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Chihuahua
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Costa_Rica
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Creston
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cuiaba
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Curacao
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Danmarkshavn
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Dawson
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Dawson_Creek
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Denver
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Detroit
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Dominica
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Edmonton
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Eirunepe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/El_Salvador
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Fortaleza
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Glace_Bay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Godthab
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Goose_Bay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Grand_Turk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Grenada
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Guadeloupe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Guatemala
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Guayaquil
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Guyana
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Halifax
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Havana
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Hermosillo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Indianapolis
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Knox
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Marengo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Petersburg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Tell_City
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Vevay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Vincennes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Winamac
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Inuvik
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Iqaluit
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Jamaica
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Juneau
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Kentucky
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Kentucky/Louisville
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Kentucky/Monticello
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/La_Paz
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Lima
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Los_Angeles
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Maceio
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Managua
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Manaus
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Martinique
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Matamoros
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Mazatlan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Menominee
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Merida
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Metlakatla
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Mexico_City
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Miquelon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Moncton
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Monterrey
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Montevideo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Montreal
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Montserrat
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Nassau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/New_York
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Nipigon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Nome
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Noronha
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/North_Dakota
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/North_Dakota/Beulah
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/North_Dakota/Center
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/North_Dakota/New_Salem
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Ojinaga
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Panama
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Pangnirtung
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Paramaribo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Phoenix
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Port-au-Prince
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Port_of_Spain
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Porto_Velho
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Puerto_Rico
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Rainy_River
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Rankin_Inlet
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Recife
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Regina
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Resolute
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Rio_Branco
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Santa_Isabel
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Santarem
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Santiago
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Santo_Domingo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Sao_Paulo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Scoresbysund
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Sitka
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Johns
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Kitts
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Lucia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Thomas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Vincent
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Swift_Current
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Tegucigalpa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Thule
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Thunder_Bay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Tijuana
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Toronto
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Tortola
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Vancouver
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Whitehorse
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Winnipeg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Yakutat
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Yellowknife
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Casey
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Davis
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/DumontDUrville
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Macquarie
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Mawson
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/McMurdo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Palmer
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Rothera
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Syowa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Vostok
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Aden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Almaty
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Amman
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Anadyr
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Aqtau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Aqtobe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Ashgabat
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Baghdad
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Bahrain
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Baku
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Bangkok
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Beirut
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Bishkek
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Brunei
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Choibalsan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Chongqing
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Colombo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Damascus
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Dhaka
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Dili
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Dubai
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Dushanbe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Gaza
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Harbin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Hebron
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Ho_Chi_Minh
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Hong_Kong
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Hovd
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Irkutsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Jakarta
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Jayapura
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Jerusalem
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kabul
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kamchatka
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Karachi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kashgar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kathmandu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kolkata
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Krasnoyarsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kuala_Lumpur
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kuching
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kuwait
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Macau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Magadan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Makassar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Manila
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Muscat
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Nicosia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Novokuznetsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Novosibirsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Omsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Oral
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Phnom_Penh
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Pontianak
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Pyongyang
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Qatar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Qyzylorda
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Rangoon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Riyadh
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Riyadh87
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Riyadh88
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Riyadh89
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Sakhalin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Samarkand
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Seoul
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Shanghai
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Singapore
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Taipei
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Tashkent
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Tbilisi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Tehran
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Thimphu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Tokyo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Ulaanbaatar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Urumqi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Vientiane
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Vladivostok
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Yakutsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Yekaterinburg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Yerevan
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Azores
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Bermuda
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Canary
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Cape_Verde
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Faroe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Madeira
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Reykjavik
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/South_Georgia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/St_Helena
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Stanley
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Adelaide
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Brisbane
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Broken_Hill
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Currie
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Darwin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Eucla
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Hobart
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Lindeman
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Lord_Howe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Melbourne
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Perth
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Sydney
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/CET
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/CST6CDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/EET
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/EST
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/EST5EDT
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+1
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+10
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+11
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+12
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+2
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+3
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+4
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+5
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+6
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+7
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+8
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+9
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-1
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-10
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-11
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-12
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-13
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-14
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-2
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-3
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-4
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-5
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-6
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-7
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-8
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-9
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/UCT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/UTC
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Amsterdam
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Andorra
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Athens
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Belgrade
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Berlin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Brussels
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Bucharest
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Budapest
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Chisinau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Copenhagen
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Dublin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Gibraltar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Helsinki
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Istanbul
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Kaliningrad
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Kiev
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Lisbon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/London
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Luxembourg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Madrid
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Malta
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Minsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Monaco
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Moscow
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Oslo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Paris
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Prague
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Riga
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Rome
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Samara
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Simferopol
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Sofia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Stockholm
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Tallinn
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Tirane
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Uzhgorod
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Vaduz
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Vienna
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Vilnius
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Volgograd
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Warsaw
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Zaporozhye
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Zurich
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/GMT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/HST
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Antananarivo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Chagos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Christmas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Cocos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Comoro
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Kerguelen
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Mahe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Maldives
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Mauritius
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Mayotte
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Reunion
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/MET
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/MST
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/MST7MDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/PST8PDT
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Apia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Auckland
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Chatham
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Chuuk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Easter
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Efate
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Enderbury
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Fakaofo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Fiji
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Funafuti
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Galapagos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Gambier
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Guadalcanal
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Guam
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Honolulu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Johnston
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Kiritimati
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Kosrae
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Kwajalein
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Majuro
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Marquesas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Midway
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Nauru
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Niue
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Norfolk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Noumea
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Pago_Pago
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Palau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Pitcairn
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Pohnpei
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Port_Moresby
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Rarotonga
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Saipan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Tahiti
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Tarawa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Tongatapu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Wake
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Wallis
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/AST4
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/AST4ADT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/CST6
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/CST6CDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/EST5
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/EST5EDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/HST10
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/MST7
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/MST7MDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/PST8
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/PST8PDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/YST9
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/YST9YDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/WET
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/ZoneInfoMappings
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/desktop
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/desktop/sun_java.desktop
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/desktop/sun_java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/i386
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/i386/ns7
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/i386/ns7-gcc29
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/i386/ns7-gcc29/libjavaplugin_oji.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/i386/ns7/libjavaplugin_oji.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/ct.sym
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/dt.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/htmlconverter.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/ir.idl
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/jconsole.jar
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/jexec
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/orb.idl
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/sa-jdi.jar
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/lib/tools.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/tools.pack
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/etc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/etc/visualvm.clusters
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/etc/visualvm.conf
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/.lastModified
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/VERSION.txt
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-netbeans-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-netbeans-modules-options-api.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-netbeans-modules-queries.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-explorer.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-loaders.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-modules.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-text.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-util.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-api-annotations-common.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-api-progress.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-api-visual.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-io-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-multiview.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-output2.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-windows.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-applemenu.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-autoupdate-services.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-autoupdate-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-core-kit.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-editor-mimelookup-impl.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-editor-mimelookup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-favorites.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-javahelp.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-keyring-impl.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-keyring.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-masterfs.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-options-api.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-options-keymap.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-print.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-progress-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-queries.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-sendopts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-settings.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-spi-actions.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-spi-quicksearch.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-swing-outline.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-swing-plaf.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-swing-tabcontrol.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-actions.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-awt.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-compat.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-dialogs.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-explorer.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-io.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-loaders.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-nodes.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-options.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-text.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-util-enumerations.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-windows.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/core.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale/core_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale/core_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale/org-openide-filesystems_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale/org-openide-filesystems_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/org-openide-filesystems.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/docs
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/boot.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/boot_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/boot_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-modules_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-modules_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-util-lookup_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-util-lookup_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-util_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-util_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/nbexec
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/org-openide-modules.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/org-openide-util-lookup.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/org-openide-util.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/jh-2.0_05.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/locale/updater_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/locale/updater_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/updater.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-annotations-common_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-annotations-common_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-progress_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-progress_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-visual_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-visual_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-execution_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-execution_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-io-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-io-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-multiview_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-multiview_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-output2_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-output2_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-windows_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-windows_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-applemenu_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-applemenu_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-autoupdate-services_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-autoupdate-services_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-autoupdate-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-autoupdate-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-core-kit_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-core-kit_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-editor-mimelookup-impl_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-editor-mimelookup-impl_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-editor-mimelookup_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-editor-mimelookup_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-favorites_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-favorites_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-javahelp_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-javahelp_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-keyring-impl_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-keyring-impl_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-keyring_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-keyring_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-masterfs_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-masterfs_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-options-api_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-options-api_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-options-keymap_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-options-keymap_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-print_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-print_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-progress-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-progress-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-queries_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-queries_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-sendopts_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-sendopts_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-settings_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-settings_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-spi-actions_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-spi-actions_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-templates_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-templates_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-spi-quicksearch_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-spi-quicksearch_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-outline_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-outline_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-plaf_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-plaf_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-tabcontrol_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-tabcontrol_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-actions_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-actions_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-awt_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-awt_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-compat_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-compat_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-dialogs_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-dialogs_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-execution_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-execution_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-explorer_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-explorer_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-io_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-io_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-loaders_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-loaders_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-nodes_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-nodes_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-options_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-options_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-text_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-text_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-util-enumerations_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-util-enumerations_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-windows_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-windows_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-api-annotations-common.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-api-progress.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-api-visual.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-execution.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-io-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-multiview.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-output2.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-windows.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-applemenu.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-autoupdate-services.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-autoupdate-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-core-kit.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-editor-mimelookup-impl.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-editor-mimelookup.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-favorites.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-javahelp.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-keyring-impl.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-keyring.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-masterfs.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-options-api.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-options-keymap.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-print.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-progress-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-queries.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-sendopts.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-settings.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-spi-actions.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-spi-quicksearch.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-swing-outline.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-swing-plaf.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-swing-tabcontrol.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-actions.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-awt.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-compat.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-dialogs.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-execution.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-explorer.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-io.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-loaders.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-nodes.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-options.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-text.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-util-enumerations.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-windows.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-api-annotations-common.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-api-progress.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-api-visual.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-bootstrap.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-io-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-multiview.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-output2.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-startup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-windows.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-applemenu.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-autoupdate-services.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-autoupdate-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-core-kit.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-editor-mimelookup-impl.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-editor-mimelookup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-favorites.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-javahelp.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-keyring-impl.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-keyring.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-masterfs.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-options-api.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-options-keymap.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-print.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-progress-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-queries.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-sendopts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-settings.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-spi-actions.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-spi-quicksearch.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-swing-outline.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-swing-plaf.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-swing-tabcontrol.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-actions.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-awt.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-compat.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-dialogs.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-explorer.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-filesystems.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-io.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-loaders.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-modules.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-nodes.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-options.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-text.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-util-enumerations.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-util-lookup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-util.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-windows.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/.lastModified
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/VERSION.txt
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-lib-profiler-charts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-lib-profiler-common.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-lib-profiler-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-lib-profiler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-modules-profiler-oql.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-modules-profiler.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk15
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk15/linux
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk15/linux/libprofilerinterface.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk16/linux
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk16/linux/libprofilerinterface.so
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/jfluid-server-15.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/jfluid-server.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/locale/jfluid-server_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/locale/jfluid-server_zh_CN.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-charts_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-charts_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-common_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-common_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-modules-profiler-oql_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-modules-profiler-oql_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-modules-profiler_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-modules-profiler_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-lib-profiler-charts.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-lib-profiler-common.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-lib-profiler-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-lib-profiler.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-modules-profiler-oql.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-modules-profiler.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-lib-profiler-charts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-lib-profiler-common.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-lib-profiler-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-lib-profiler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-modules-profiler-oql.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-modules-profiler.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/.lastModified
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-api-caching.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-application-views.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-application.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-attach.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-charts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-coredump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-heapdump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-host-remote.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-host-views.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-host.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-jmx.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-jvm.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-jvmstat.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-modules-appui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-profiler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-profiling.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-sa.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-sampler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-threaddump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-tools.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-uisupport.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-api-visual.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-core-execution.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-core-output2.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-modules-core-kit.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-modules-favorites.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-modules-options-keymap.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-modules-spi-actions.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-openide-compat.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-openide-options.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-openide-util-enumerations.xml_hidden
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/com-sun-tools-visualvm-modules-startup.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/.svn_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/.svn_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/com-sun-tools-visualvm-modules-startup_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/com-sun-tools-visualvm-modules-startup_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/core_visualvm.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/all-wcprops
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-api-caching.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-application-views.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-application.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-attach.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-charts.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-core.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-coredump.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-heapdump.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-host-remote.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-host-views.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-host.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-jmx.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-jvm.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-jvmstat.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-modules-appui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-profiler.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-profiling.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-sa.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-sampler.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-threaddump.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-tools.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-uisupport.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/entries
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-api-caching_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-api-caching_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-application-views_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-application-views_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-application_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-application_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-attach_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-attach_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-charts_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-charts_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-core_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-core_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-coredump_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-coredump_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-heapdump_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-heapdump_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host-remote_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host-remote_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host-views_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host-views_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jmx_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jmx_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jvm_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jvm_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jvmstat_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jvmstat_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-modules-appui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-modules-appui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-profiler_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-profiler_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-profiling_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-profiling_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-sa_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-sa_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-sampler_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-sampler_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-threaddump_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-threaddump_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-tools_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-tools_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-uisupport_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-uisupport_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-core-windows_visualvm.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-core_visualvm.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-.svn_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-.svn_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-profiler_visualvm.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-prop-base_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-prop-base_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-props_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-props_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-text-base_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-text-base_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-tmp_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-tmp_zh_CN.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-api-caching.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-application-views.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-application.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-attach.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-charts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-coredump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-heapdump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-host-remote.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-host-views.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-host.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-jmx.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-jvm.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-jvmstat.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-modules-appui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-modules-startup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-profiler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-profiling.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-sa.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-sampler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-threaddump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-tools.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-uisupport.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/appletviewer.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/apt.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/extcheck.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/idlj.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jar.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jarsigner.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/java.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/javac.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/javadoc.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/javah.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/javap.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/javaws.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jconsole.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jdb.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jhat.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jinfo.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jmap.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jps.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jrunscript.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jsadebugd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jstack.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jstat.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jstatd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jvisualvm.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/keytool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/native2ascii.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/orbd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/pack200.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/policytool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/rmic.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/rmid.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/rmiregistry.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/schemagen.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/serialver.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/servertool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/tnameserv.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/unpack200.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/wsgen.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/wsimport.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/xjc.1
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/appletviewer.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/apt.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/extcheck.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/idlj.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jar.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jarsigner.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/java.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javac.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javadoc.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javah.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javap.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javaws.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jconsole.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jdb.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jhat.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jinfo.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jmap.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jps.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jrunscript.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jsadebugd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jstack.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jstat.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jstatd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jvisualvm.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/keytool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/native2ascii.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/orbd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/pack200.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/policytool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/rmic.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/rmid.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/rmiregistry.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/schemagen.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/serialver.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/servertool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/tnameserv.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/unpack200.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/wsgen.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/wsimport.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/xjc.1
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/src.zip




%post -p /bin/sh
#
    # Make sure any new files are created with a secure access mask.  Do not use
    # chmod, since that would also change the rights of any existing files, and
    # we are only interested in setting the rights for new files.
    #
    umask 022

    #
    # The package assumes that Gnome is either installed, or going to be
    # installed, so if nothing currently exists, then install in the default
    # location.
    #
    # NOTE: These variables must be defined before all the shell function macros
    #       are included.
    #
    if [ -z "${GNOMEDIR}" ]; then
        GNOMEDIR=/usr
    fi

    #
    # RPM_INSTALL_PREFIX doesn't seem to be set by "alien" so the following
    # minor kludge allows some functionality on debian-like systems (such
    # a Ubuntu) which don't support packages.
    #
    if [ -z "${RPM_INSTALL_PREFIX}" ]; then
	RPM_INSTALL_PREFIX="/usr/java"
    fi

    #
    # Gross kludge for old SuSE distros: Even though they set the environment
    # variable GNOMEDIR to /opt/gnome, Gnome may really be in /opt/gnome2.
    # Go figure,... (I feel so unclean....)
    #
    if [ "${GNOMEDIR}" = "/opt/gnome" ] && [ -d "/opt/gnome2" ]; then
	GNOMEDIR="/opt/gnome2"
    fi

    INSTALL_JRE_PATH=${RPM_INSTALL_PREFIX}/jdk1.6.0_45
    if [ -e ${INSTALL_JRE_PATH}/jre/bin/java ]; then
	INSTALL_JRE_PATH=${INSTALL_JRE_PATH}/jre
    fi

    #
    # Add the shell function and related variables used by the post-install.
    #
    ERROR_MISSING_PARAM=1000
ERROR_MISSING_PACKED_JAR=1001
ERROR_BAD_PARAM=1002
ERROR_MISSING_UNPACK200=1003
unpack_jars() {
    status=0
    if [ $# -lt 3 ]; then
        printf "Error: usage - no packed files specified, nothing to do:\n\n" \
								>> /dev/stderr
        printf "\t unpack_jars\n" "$*"                          >> /dev/stderr
        status=${ERROR_MISSING_PARAM}
    else
        unpack200=$1
        root=$2
        shift 2
        if [ -f ${unpack200} ]; then
            if [ -d ${root} ]; then                
                printf "Unpacking JAR files...\n"
                for file in $*; do
                    pack_file=`basename ${file} .jar`.pack
                    pack_src=${root}/`dirname ${file}`/${pack_file}
                    jar_dest=${root}/${file}
                    printf "\t%s...\n" "`basename ${file}`"
                    ${unpack200} ${pack_src} ${jar_dest}
                    if [ ! -f ${jar_dest} ]; then
                        printf "Error: unpack could not create JAR file:\n\n" \
								>> /dev/stderr
                        printf "\t%s\n\n" "${jar_dest}"		>> /dev/stderr
                        printf "Please refer to the "		>> /dev/stderr
			printf "Troubleshooting section of "    >> /dev/stderr
                        printf "the Installation "              >> /dev/stderr
                        printf "Instructions\n"                 >> /dev/stderr
                        printf "on the download page.\n"        >> /dev/stderr
                        status=${ERROR_MISSING_PACKED_JAR}
                    fi
                    rm -f ${pack_src}
                done
            else
                printf "Error: usage - the base path for the "  >> /dev/stderr
                printf "packed JAR files is invalid:\n\n"	>> /dev/stderr
                printf "\tunpack_jars %s\n" "$*"		>> /dev/stderr
                status=${ERROR_BAD_PARAM}
            fi
        else
            printf "Error: unpack200 - command could not be found.\n\n" \
								>> /dev/stderr
            printf "Please refer to the Troubleshooting "       >> /dev/stderr
            printf "section of the"                             >> /dev/stderr
            printf "Installation Instructions\n"                >> /dev/stderr
            printf "on the download page.\n"                    >> /dev/stderr
            status=${ERROR_MISSING_UNPACK200}
        fi
    fi
    return ${status}
}
    NS_COMMENT1="#--Netscape Communications Corporation MIME Information"
NS_COMMENT2="#Do not delete the above line. It is used to identify the file type."
NS_COMMENT3="#mime types added by Netscape Helper"
UpdateMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    command="$3"
    if [ -z "`grep -E \"^${mime_type}; ${command}$\" \"${mailcap_file}\" 2> /dev/null`" ]; then
        mc_comment="# Java Web Start"
        mc_text=
        if [ -w "${mailcap_file}" ]; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
        fi
        if [ -w "`dirname \"${mailcap_file}\"`" ]; then
            mc_text="${mc_text:+${mc_text}\n}${mime_type}; ${command}"
            printf "%s" "${mc_text}" > "${mailcap_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mailcap_file}"
            echo "Check permissions."
        fi
    fi
}
RemoveMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    mc_comment="# Java Web Start"
    if [ -w "${mailcap_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mailcap_file}\"`" ] ; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
            if [ `echo "${mc_text}" | tr -d '[:space:]' | wc -c` -gt 0 ]; then
                echo "${mc_text}" > "${mailcap_file}"
            else
                rm -f "${mailcap_file}"
            fi
        fi
    fi
}
UpdateMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    desc="$3"
    shift 3
    exts="$*"
    JNLP_ENTRY="type=${mime_type} desc=\"${desc}\" exts=\"${exts}\""
    if [ ! -w "${mime_file}" ]; then
        if [ -w `dirname ${mime_file}` ]; then
            echo "${NS_COMMENT1}"  > "${mime_file}"
            echo "${NS_COMMENT2}" >> "${mime_file}"
            echo "${NS_COMMENT3}" >> "${mime_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mime_file}"
            echo "Check permissions."
            return
        fi
    fi
    if [ -z "`grep -E \"^[^#]*${mime_type}\" \"${mime_file}\"`" ]; then
        echo ${JNLP_ENTRY} >> "${mime_file}"
    fi
}
RemoveMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    if [ -w "${mime_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mime_file}\"`" ]; then
            regexp="(${mime_type})|(^${NS_COMMENT1}$)|(^${NS_COMMENT2}$)|(^${NS_COMMENT3}$)"
            if [ `grep -Ev "${regexp}" "${mime_file}" | \
                 tr -d '[:space:]' | wc -c` -gt 0 ]
            then
                mt_text="`grep -v \"${mime_type}\" \"${mime_file}\"`"
                echo "${mt_text}" > "${mime_file}"
            else
                rm -f "${mime_file}"
            fi
        fi
    fi
}
    JDK_DESKTOP="${INSTALL_JRE_PATH}/lib/desktop"
JDK_ICONS="${JDK_DESKTOP}/icons"
JDK_APPS="${JDK_DESKTOP}/applications"
JDK_MIME="${JDK_DESKTOP}/mime"
SHARE_PATH="${GNOMEDIR}/share"
SHARE_ICONS="${SHARE_PATH}/icons"
SHARE_MIME="${SHARE_PATH}/mime"
SHARE_APPS="${SHARE_PATH}/applications"
HICOLOR=hicolor
HIGHCONTRAST=HighContrast
HIGHCONTRASTINVERSE=HighContrastInverse
LOWCONTRAST=LowContrast
THEMES="${HICOLOR} ${HIGHCONTRAST} ${HIGHCONTRASTINVERSE} ${LOWCONTRAST}"
RESOLUTIONS="16x16 48x48"
TEXT_ICON="gnome-mime-text-x-java.png"
JAR_ICON="gnome-mime-application-x-java-archive.png"
JNLP_ICON="gnome-mime-application-x-java-jnlp-file.png"
JAVA_ICON="sun-java.png"
JAVAWS_ICON="sun-javaws.png"
JCONTROL_ICON="sun-jcontrol.png"
APPS_ICONS="${JAVA_ICON} ${JAVAWS_ICON} ${JCONTROL_ICON}"
MIME_ICONS="${TEXT_ICON} ${JAR_ICON} ${JNLP_ICON}"
ICONS="${APPS_ICONS} ${MIME_ICONS}"
GNOME_UTILS_DIRS="/usr/bin /opt/gnome/bin"
UPDATE_MIME_DATABASE="update-mime-database"
UPDATE_DESKTOP_DATABASE="update-desktop-database"
GTK_UPDATE_ICON_CACHE="gtk-update-icon-cache"
SHARE_CONTROL_CENTER="${SHARE_PATH}/control-center-2.0"
SHARE_CAPPLETS="${SHARE_CONTROL_CENTER}/capplets"
SHARE_MIME_INFO="${SHARE_PATH}/mime-info"
SHARE_APP_REGISTRY="${SHARE_PATH}/application-registry"
SHARE_PIXMAPS="${SHARE_PATH}/pixmaps"
UpdateIconCache() {
    _icon_theme_root=$1
    if [ -f ${_icon_theme_root}/icon-theme.cache ]; then
	for _dir in ${GNOME_UTILS_DIRS}; do
	    if [ -x ${_dir}/${GTK_UPDATE_ICON_CACHE} ]; then
		${_dir}/${GTK_UPDATE_ICON_CACHE} ${_icon_theme_root} \
		    > /dev/null 2>&1
		break
	    fi
	done
	touch ${_icon_theme_root}
	for _dir in ${RESOLUTIONS}; do
	    if [ -d ${_icon_theme_root}/${_dir} ]; then
		touch ${_icon_theme_root}/${_dir}
	    fi
        done
    fi
}
UpdateDesktopDatabase() {
    _desktop_root=$1
    if [ -f ${_desktop_root}/mimeinfo.cache ]; then
	for _dir in ${GNOME_UTILS_DIRS}; do
	    if [ -x ${_dir}/${UPDATE_DESKTOP_DATABASE} ]; then
		${_dir}/${UPDATE_DESKTOP_DATABASE} ${_desktop_root} \
		   > /dev/null 2>&1
		break
	    fi
	done
    fi
}
UpdateMimeDatabase() {
    _mime_root=$1
    if [ -d ${_mime_root}/packages ]; then
	for _dir in ${GNOME_UTILS_DIRS}; do
	    if [ -x ${_dir}/${UPDATE_MIME_DATABASE} ]; then
		${_dir}/${UPDATE_MIME_DATABASE} ${_mime_root} > /dev/null 2>&1
		break
	    fi
	done
    fi
}
InstallGnomeIcons() {
    for _theme in ${THEMES}; do
	if [ -d ${SHARE_ICONS}/${_theme} ]; then
	    for _res in ${RESOLUTIONS}; do
		mkdir -p ${SHARE_ICONS}/${_theme}/${_res}/apps
		for _icon in ${APPS_ICONS}; do
		    cp -f ${JDK_ICONS}/${_theme}/${_res}/apps/${_icon} \
			  ${SHARE_ICONS}/${_theme}/${_res}/apps/${_icon}
		done
		mkdir -p ${SHARE_ICONS}/${_theme}/${_res}/mimetypes
		for _icon in ${MIME_ICONS}; do
		    cp -f ${JDK_ICONS}/${_theme}/${_res}/mimetypes/${_icon} \
			  ${SHARE_ICONS}/${_theme}/${_res}/mimetypes/${_icon}
		done
	    done
	    UpdateIconCache ${SHARE_ICONS}/${_theme}
	fi
    done
    if [ -d ${SHARE_PIXMAPS} ]; then
	for _icon in ${APPS_ICONS}; do
	    cp -f ${JDK_ICONS}/${HICOLOR}/48x48/apps/${_icon} \
		  ${SHARE_PIXMAPS}/${_icon}
	done
	cp -f ${JDK_ICONS}/${HICOLOR}/48x48/mimetypes/${TEXT_ICON} \
	      ${SHARE_PIXMAPS}/x-java.png
	cp -f ${JDK_ICONS}/${HICOLOR}/48x48/mimetypes/${JAR_ICON} \
	      ${SHARE_PIXMAPS}/x-java-archive.png
	cp -f ${JDK_ICONS}/${HICOLOR}/48x48/mimetypes/${JNLP_ICON} \
	      ${SHARE_PIXMAPS}/x-java-jnlp-file.png
    fi
}
RemoveGnomeIcons() {
    for _theme in ${THEMES}; do
	for _res in ${RESOLUTIONS}; do
	    for _icon in ${APPS_ICONS}; do
		rm -f ${SHARE_ICONS}/${_theme}/${_res}/apps/${_icon}
	    done
	    for _icon in ${MIME_ICONS}; do
		rm -f ${SHARE_ICONS}/${_theme}/${_res}/mimetypes/${_icon}
	    done
	done
	UpdateIconCache ${SHARE_ICONS}/${_theme}
    done
    if [ -d ${SHARE_PIXMAPS} ]; then
	for _icon in ${APPS_ICONS}; do
	    rm -f ${SHARE_PIXMAPS}/${_icon}
	done
	rm -f ${SHARE_PIXMAPS}/x-java.png
	rm -f ${SHARE_PIXMAPS}/x-java-archive.png
	rm -f ${SHARE_PIXMAPS}/x-java-jnlp-file.png
    fi
}
InstallGnomeDesktop() {
    _file=$1
    mkdir -p ${SHARE_APPS}
    cp -f ${JDK_APPS}/${_file} ${SHARE_APPS}/${_file}
    if [ "${_file}" = "sun_java.desktop" ]; then
	if [ -d ${SHARE_CAPPLETS} ]; then
	    cp -f ${JDK_APPS}/${_file} ${SHARE_CAPPLETS}/${_file}
	fi
    fi
}
RemoveGnomeDesktop() {
    _file=$1
    rm -f ${SHARE_APPS}/${_file}
    rm -f ${SHARE_CAPPLETS}/${_file}
}
InstallLegacyMimetype() {
    _mime_type=$1
    _extension=$2
    _name=$3
    _command=$4
    _icon=$5
    _description=$6
    cat <<- end_of_keys_file > ${SHARE_MIME_INFO}/${_name}.keys
	${_mime_type}:
	    description=${_description}
	    icon_filename=${_icon}
	    default_action_type=application
	    default_application_id=${_name}
	    short_list_application_user_additions=${_name}
	end_of_keys_file
    cat <<- end_of_mime_file > ${SHARE_MIME_INFO}/${_name}.mime
	${_mime_type}
	    ext: ${_extension}
	end_of_mime_file
    cat <<- end_of_apps_file > ${SHARE_APP_REGISTRY}/${_name}.applications
	${_name}
	    command=${_command}
	    name=${_name}
	    can_open_multiple_files=false
	    requires_terminal=false
	    mime_types=${_mime_type}
	end_of_apps_file
}
RemoveLegacyMimetype() {
    _name=$1
    rm -f ${SHARE_MIME_INFO}/${_name}.keys
    rm -f ${SHARE_MIME_INFO}/${_name}.mime
    rm -f ${SHARE_APP_REGISTRY}/${_name}.applications
}
InstallGnomeMimetypes() {
    if [ -d ${SHARE_MIME} ]; then
	cp -f ${JDK_MIME}/packages/x-java-archive.xml \
	      ${SHARE_MIME}/packages/x-java-archive.xml
	cp -f ${JDK_MIME}/packages/x-java-jnlp-file.xml \
	      ${SHARE_MIME}/packages/x-java-jnlp-file.xml
    fi
    UpdateMimeDatabase ${SHARE_MIME}
    if [ -d ${SHARE_MIME_INFO} ] || [ -d ${SHARE_APP_REGISTRY} ]; then
	mkdir -p ${SHARE_MIME_INFO}
	mkdir -p ${SHARE_APP_REGISTRY}
	InstallLegacyMimetype application/x-java-archive \
                 jar              \
                 java-archive     \
                 "java -jar"      \
                 x-java-archive.png     \
		 "Java Archive"
	InstallLegacyMimetype application/x-java-jnlp-file \
                 jnlp                \
                 java-web-start      \
                 javaws              \
                 x-java-jnlp-file.png        \
                 "Java Web Start Application"
    fi
}
RemoveGnomeMimetypes() {
    rm -f ${SHARE_MIME}/packages/x-java-archive.xml
    rm -f ${SHARE_MIME}/packages/x-java-jnlp-file.xml
    UpdateMimeDatabase ${SHARE_MIME}
    if [ -d ${SHARE_MIME_INFO} ] || [ -d ${SHARE_APP_REGISTRY} ]; then
	RemoveLegacyMimetype java-archive
	RemoveLegacyMimetype java-web-start
    fi
}
IntegrateWithGnome() {
    InstallGnomeIcons
    InstallGnomeDesktop sun_java.desktop
    InstallGnomeDesktop sun-java.desktop
    InstallGnomeDesktop sun-javaws.desktop
    UpdateDesktopDatabase ${SHARE_APPS}
    InstallGnomeMimetypes
}
DisintegrateWithGnome() {
    RemoveGnomeIcons
    RemoveGnomeDesktop sun_java.desktop
    RemoveGnomeDesktop sun-java.desktop
    RemoveGnomeDesktop sun-javaws.desktop
    UpdateDesktopDatabase ${SHARE_APPS}
    RemoveGnomeMimetypes
}
    MOST_DIGITS="[1-9]"
ALL_DIGITS="[0-9]"
COUNTING_NUMBER="${MOST_DIGITS}${ALL_DIGITS}*\|0"
VALID_NON_NUMERIC="[-_.a-zA-Z]"
VALID_CHARS="[-_.a-zA-Z0-9]"
MAJOR_RULE="\(${MOST_DIGITS}${ALL_DIGITS}*\)"
MINOR_RULE="\(${COUNTING_NUMBER}\)"
MICRO_RULE="\(${COUNTING_NUMBER}\)"
UPDATE_RULE="\(${MOST_DIGITS}${ALL_DIGITS}\|0${ALL_DIGITS}\)"
NON_FCS_ID_RULE="\([a-zA-Z0-9]*\)"
MIN_VERSION_ID_RULE="${MAJOR_RULE}\.${MINOR_RULE}\.${MICRO_RULE}"
FCS_VERSION_ID_RULE="${MIN_VERSION_ID_RULE}\(_${UPDATE_RULE}\)\?"
VERSION_ID_RULE="${FCS_VERSION_ID_RULE}\(-${NON_FCS_ID_RULE}\)\?"
NAME_ID_RULE="${VALID_CHARS}*${VALID_NON_NUMERIC}"
KNOWN_GOOD_NAME_LIST="java jdk jre j2sdk j2re"
PRS_ERROR_BAD_PARAMS=2000
expand_version() {
    status=0
    if [ $# -eq 0 ]; then
        read release remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${release}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${release}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        release=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        \printf "\t expand_version\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        format="%d\t%d\t%d\t%d\n"
        echo ${release} | sed -e "s/_/\./g" | \
          awk -v format="${format}" 'BEGIN { FS = "." } { printf format, $1, $2, $3, $4 }'
    fi
    return ${status}
}
parse_release() {
    status=0
    if [ $# -eq 0 ]; then
        read string remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${string}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${string}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        string=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t parse_release %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        version_id=`expr "${string}" : "${NAME_ID_RULE}\(${VERSION_ID_RULE}\)\$"`
        if [ -n "${version_id}" ]; then
            name_id=`expr "${string}" : "\(${NAME_ID_RULE}\)${VERSION_ID_RULE}\$"`
            fcs_part=`expr "${string}" : "${NAME_ID_RULE}\(${FCS_VERSION_ID_RULE}\).*\$"`
            non_fcs_part=`expr "${version_id}" : "[^-]*-\(${NON_FCS_ID_RULE}\)\$"`
	    printf "%s\t%s\t%s\n" "${name_id}" "${fcs_part}" "${non_fcs_part}"
        fi
    fi
    return ${status}
}
UNKNOWN_NAME_WEIGHT=1000
get_name_weight() {
    status=0
    if [ "$1" = "-" ]; then
        read name good_names
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        else
            shift 1
            if [ $# -gt 0 ]; then
                good_names="$*"
            fi
            if [ -z "${name}" ]; then
                printf "Error: usage - function requires input!\n" >> /dev/stderr
                status=${PRS_ERROR_BAD_PARAMS}
            fi
        fi
    elif [ $# -gt 1 ]; then
        name=$1
        shift 1
        good_names="$*"
    else
        printf "Error: usage - function takes 2+ parameters:\n\n" >> /dev/stderr
        printf "\t get_name_weight %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -n "${good_names}" ]; then
            length=`expr length "${good_names}"`
            pos=`expr "${good_names}" : ".*\<${name}\>"`
            if [ ${pos} -gt 0 ]; then
                expr substr "${good_names}" 1 ${pos} | wc -w | tr -d "[:space:]"
            else
                echo ${UNKNOWN_NAME_WEIGHT}
            fi
        else
            echo ${UNKNOWN_NAME_WEIGHT}
        fi
    fi
    return ${status}
}
HAS_FCS_WEIGHT=0
HAS_ODD_FCS_WEIGHT=1
HAS_RC_WEIGHT=100
HAS_ODD_RC_WEIGHT=101
HAS_BETA_WEIGHT=300
HAS_ODD_BETA_WEIGHT=301
HAS_EA_WEIGHT=500
HAS_ODD_EA_WEIGHT=501
HAS_INTRNAL_WEIGHT=2000
HAS_VERY_ODD_WEIGHT=9999
get_non_fcs_weight() {
    status=0
    if [ $# -eq 0 ]; then
        read non_fcs_part remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${non_fcs_part}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        non_fcs_part=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t get_non_fcs_weight \n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -z "${non_fcs_part}" ]; then
            echo ${HAS_FCS_WEIGHT}
        else
            case "${non_fcs_part}" in
                fcs)
                    echo ${HAS_ODD_FCS_WEIGHT}
                    ;;
                rc)
                    echo ${HAS_RC_WEIGHT}
                    ;;
                rc[0-9] | rc[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "rc\([0-9]*\)$"`
                    echo `expr ${HAS_RC_WEIGHT} - ${count}`
                    ;;
                rc*)
                    echo ${HAS_ODD_RC_WEIGHT}
                    ;;
                beta)
                    echo ${HAS_BETA_WEIGHT}
                    ;;
                beta[0-9] | beta[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "beta\([0-9]*\)$"`
                    echo `expr ${HAS_BETA_WEIGHT} - ${count}`
                    ;;
                beta*)
                    echo ${HAS_ODD_BETA_WEIGHT}
                    ;;
                ea)
                    echo ${HAS_EA_WEIGHT}
                    ;;
                ea[0-9] | ea[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "ea\([0-9]*\)$"`
                    echo `expr ${HAS_EA_WEIGHT} - ${count}`
                    ;;
                ea*)
                    echo ${HAS_ODD_EA_WEIGHT}
                    ;;
                internal)
                    echo ${HAS_INTRNAL_WEIGHT}
                    ;;
                internal[0-9] | internal[0-9][0-9] | internal[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "internal\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                b[0-9] | b[0-9][0-9] | b[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "b\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                *)
                    echo ${HAS_VERY_ODD_WEIGHT}
                    ;;
            esac
        fi
    fi
    return ${status}
}
    get_path_weight() {
    good_list="$1"
    path=$2
    release=`basename ${path}`
    parts="`parse_release ${release}`"
    if [ $? -eq 0 ]; then
        name=`echo "${parts}" | cut -f1`
        version=`echo "${parts}" | cut -f2`
        non_fcs=`echo "${parts}" | cut -f3`
        if [ -n "${version}" ]; then
           v_weight=`echo ${version} | expand_version`
           n_weight=`echo ${name} | get_name_weight - "${good_list}"`
           o_weight=`echo ${non_fcs} | get_non_fcs_weight`
           printf "%4d  %4d  %4d  %4d  %4d  %4d  %s\n" \
                  ${v_weight} ${n_weight} ${o_weight} "${path}"
        fi
    fi
}
get_weighted_list() {
    good_list=
    verify=
    stdio=
    status=0
    check=true
    while [ -n "${check}" ]; do
        if [ $# -gt 0 ]; then
            case "$1" in
                -g)
                    good_list="$2"
                    shift 2
                    ;;
                --good-list=*)
                    length=`expr length "$1"`
                    remove=`expr \( length "--good-list=" \) + 1`
                    good_list="`expr substr \"$1\" ${remove} ${length}`"
                    shift 1
                    ;;
                -v | --verify)
                    verify=true
                    shift 1
                    ;;
                --)
                    shift 1
                    check=
                    ;;
                -)
                    shift 1
                    stdio=true
                    ;;
                -*)
                    printf "Error: usage - unknown parameter:\n\n" \
								>> /dev/stderr
                    printf "\t%s : %s\n" "$1" "$*"		>> /dev/stderr
                    status=${PRS_ERROR_BAD_PARAMS}
                    check=
                    ;;
                *)
                    check=
                    ;;
            esac
        else
            check=
        fi
    done
    if [ $# -eq 0 ] || [ -n "${stdio}" ]; then
        read line
        while [ -n "${line}" ]; do
            if [ -z "${verify}" ] || [ -f ${line}/bin/java ]; then
                get_path_weight "${good_list}" ${line}
            fi
            read line
        done
    fi
    while [ $# -gt 0 ]; do
        if [ -z "${verify}" ] || [ -f $1/bin/java ]; then
            get_path_weight "${good_list}" $1
        fi
        shift 1
    done
    return ${status}
}
_compare_java_by_weight() {
    compare=0
    if [ $# -ne 0 ]; then
        if [ $# -eq 1 ]; then
            compare=1
        else
            left=$1
            right=$2
            shift 2
            good="$*"
            list=`get_weighted_list --good-list="${good}" \
                    ${left} ${right} | sort -u -k1n -k2n -k3n -k4n -k5rn -k6rn`
            if [ `echo "${list}" | wc -l | tr -d "[:space:]"` -ne 1 ]; then
                compare=-1
                latest=`echo "${list}" | tail -n 1 | cut -c 37-`
                if [ "${left}" = "${latest}" ]; then
                    compare=1
                fi
            fi
        fi
    fi
    echo ${compare}
}
compare_java_by_version() {
    _compare_java_by_weight $1 $2
}
compare_java_by_release() {
    _compare_java_by_weight $1 $2 ${KNOWN_GOOD_NAME_LIST}
}
find_latest_release() {
    if [ -d /usr/java ]; then
        latest_release=`find /usr/java/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
    fi
    if [ -d "${RPM_INSTALL_PREFIX}" ] && \
       [ "/usr/java" != "${RPM_INSTALL_PREFIX}" ]
    then 
        prefix_release=`find ${RPM_INSTALL_PREFIX}/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
        if [ `compare_java_by_release ${latest_release} ${prefix_release}` -lt 0 ]; then
            latest_release=${prefix_release}
        fi
    fi
    echo ${latest_release}
}
get_javaws() {
    path=$1
    if [ `compare_java_by_version ${path} version-1.5.0` -ge 0 ] &&
       [ -f ${path}/bin/javaws ]
    then
        path=${path}/bin/javaws
    elif [ `compare_java_by_version ${path} version-1.4.2` -ge 0 ]; then
        if [ -f ${path}/jre/javaws/javaws ]; then
            path=${path}/jre/javaws/javaws
        elif [ -f ${path}/javaws/javaws ]; then
            path=${path}/javaws/javaws
        else
            path=
        fi
    else
        path=
    fi
    echo ${path}
}
    LINK_ERROR_BAD_PARAMS=3000
LINK_ERROR_DEAD_LINK=3001
LINK_ERROR_FILE_NOT_FOUND=3002
dereference() {
    status=0
    if [ "$1" = "-f" ] || [ "$1" = "--follow" ]; then
        follow="--follow"
        shift 1
    fi
    if [ $# -ge 1 ]; then
        path="$*"
        if [ -e "${path}" ]; then
            parent="`cd \`dirname \"${path}\"\`; pwd`"
            child="`basename \"${path}\"`"
            if [ "${parent}" != "${child}" ]; then
                path="${parent}/${child}"
            fi
            if [ -h "${path}" ]; then
                path=`ls -l "${path}" | sed -e "s#^.*${path} -> ##"`
                if [ "`expr substr \"${path}\" 1 1`" != "/" ]; then
                    path="${parent}/${path}"
                fi
                if [ -n "${follow}" ]; then
                    path="`dereference ${follow} ${path}`"
                fi                    
            fi
        else
            status=${LINK_ERROR_FILE_NOT_FOUND}
        fi
    fi
    echo ${path}
    return ${status}
}
setup_latest_link() {
    latest=$1
    link=$2
    if [ -h "${link}" ]; then
        reference="`dereference --follow ${link}`"
        if [ $? -eq 0 ]; then
            update=`compare_java_by_release "${latest}" "${reference}"`
        else
            update=1
        fi
        if [ ${update} -gt 0 ]; then
            rm -f "${link}"
        fi
    fi
    if [ ! -e "${link}" ]; then
        ln -s "${latest}" "${link}"
    fi
}
setup_default_links() {
    if [ $# -ge 2 ]; then
        latest_link="$1"
        default_link="$2"
        if [ ! -e "${default_link}" ]; then
            ln -s "${latest_link}" "${default_link}"
        fi
    fi
    if [ $# -gt 3 ]; then
        bindir="$3"
        shift 3
        for file in $*; do
            reference="`dereference --follow ${bindir}/${file}`"
            if [ $? -ne 0 ]; then
                rm -f "${bindir}/${file}"
            fi
            source="${default_link}/bin/${file}"
            if [ "${file}" = "javaws" ]; then
                source="`get_javaws \"${default_link}\"`"
            fi
            if [ -n "${source}" ] && [ ! -e "${bindir}/${file}" ]; then
                ln -s "${source}" "${bindir}/${file}"
            fi
        done
    fi
}
cleanup_default_links() {
    if [ $# -ge 1 ]; then
        default_link=$1
        if [ $# -gt 2 ]; then
            bindir="$2"
            shift 2
            for file in $*; do
                reference="`dereference \"${bindir}/${file}\"`"
                if [ $? -ne 0 ] ||
                   [ "${reference}" = "${default_link}/bin/${file}" ]
                then
                    rm -f "${bindir}/${file}"
                fi
            done
        fi
        rm -f "${default_link}"
    fi
}

    #
    # Unpack the packed JAR files.
    #
    unpack_jars "${RPM_INSTALL_PREFIX}/jdk1.6.0_45/bin/unpack200" \
                "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" \
                jre/lib/rt.jar jre/lib/jsse.jar jre/lib/charsets.jar lib/tools.jar jre/lib/ext/localedata.jar jre/lib/plugin.jar jre/lib/javaws.jar jre/lib/deploy.jar

    # fix for: 4728032 - Install needs to generate shared class files
    ${RPM_INSTALL_PREFIX}/jdk1.6.0_45/bin/java -client -Xshare:dump > /dev/null 2>&1


    #
    # Find out what version of Java is the latest.  Don't do any system
    # integration unless this is the latest version.  Otherwise, we make it
    # difficult for future installers.
    #
    LATEST_JAVA_PATH="`find_latest_release`"
    if [ "${LATEST_JAVA_PATH}" == "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ] ||
       [ "${LATEST_JAVA_PATH}" == "/usr/java/jdk1.6.0_45" ]
    then
        #
        # Make sure the /usr/java/latest link points to LATEST_JAVA_PATH, and
	# update it if it doesn't.
        #
        setup_latest_link "${LATEST_JAVA_PATH}" "/usr/java/latest"

        #
        # Make sure the /usr/java/default and java javaws jcontrol javac jar javadoc exist.
	# If anything is missing, create it.
        #
        setup_default_links "/usr/java/latest" "/usr/java/default" \
                            "/usr/bin" java javaws jcontrol javac jar javadoc

        #
        # If the "latest" link is a JDK, then the latest JRE is a subdir;
	# otherwise it is the same dir.
        #
        DEFAULT_JRE_PATH="/usr/java/default"
        if [ -e "/usr/java/default/jre/bin/java" ]; then
            DEFAULT_JRE_PATH="/usr/java/default/jre"
        fi

	#
	# Perform all integrations with the freedesktop.org desktop integration
	# specifications and Gnome legacy implementations.
	#
	IntegrateWithGnome

        # setup the mailcap file
        UpdateMailcap /etc/mailcap application/x-java-jnlp-file "/usr/bin/javaws %s"

        # setup the mime.type file
        UpdateMimeTypes /etc/mime.types application/x-java-jnlp-file \
			"Java Web Start" jnlp
    fi

    #
    # If the package is being relocated, then create a link in the default
    # location (/usr/java) to the actual install directory.  Do this
    # last, so it doesn't add unnecessary complexity to the search for the
    # latest release.
    #
    if [ "${RPM_INSTALL_PREFIX}" != "/usr/java" ] &&
       ( [ ! -e "/usr/java/jdk1.6.0_45" ] || [ -h "/usr/java/jdk1.6.0_45" ] )
    then
        rm -f "/usr/java/jdk1.6.0_45"
        ln -s "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" "/usr/java/jdk1.6.0_45"
    fi

    #
    # Next, make sure the files required for the Prferences API are setup
    # correctly.  Any files from an old, uninstalled version will have left
    # files with a .rpmsave extension.  If there was an older version currently
    # installed when this version installed, there will be a set of files with
    # a .rpmnew extension.  Try to use the best possible file (i.e. save old
    # preference settings).
    #
    if [ -f /etc/.java/.systemPrefs/.system.lock.rpmsave ] &&
       [ ! -s /etc/.java/.systemPrefs/.system.lock ]
    then
        #
        # Only overwrite if old file is empty (rpmsave is only created if it is
        # non-empty).
        #
        rm -f /etc/.java/.systemPrefs/.system.lock
        mv /etc/.java/.systemPrefs/.system.lock.rpmsave \
           /etc/.java/.systemPrefs/.system.lock
    elif [ -f /etc/.java/.systemPrefs/.system.lock.rpmnew ]
    then
        if [ -s /etc/.java/.systemPrefs/.system.lock ]; then
            #
            # The existing lock is non-empty, so there is no reason to keep the
            # .rpmnew one created during this install.
            #
            rm -f /etc/.java/.systemPrefs/.system.lock.rpmnew
        else
            #
            # The existing lock is empty, so replace it with the new one.  This
            # makes future installs a little cleaner, since the file in use is
            # the file in the RPM database.
            #
            rm -f /etc/.java/.systemPrefs/.system.lock
            mv /etc/.java/.systemPrefs/.system.lock.rpmnew \
               /etc/.java/.systemPrefs/.system.lock
        fi
    fi

    if [ -f /etc/.java/.systemPrefs/.systemRootModFile.rpmsave ] &&
       [ ! -s /etc/.java/.systemPrefs/.systemRootModFile ]
    then
        #
        # Only overwrite if old file is empty (rpmsave is only created if it is
        # non-empty).
        #
        rm -f /etc/.java/.systemPrefs/.systemRootModFile
        mv /etc/.java/.systemPrefs/.systemRootModFile.rpmsave \
           /etc/.java/.systemPrefs/.systemRootModFile
    elif [ -f /etc/.java/.systemPrefs/.systemRootModFile.rpmnew ]
    then
        if [ -s /etc/.java/.systemPrefs/.systemRootModFile ]; then
            #
            # The existing lock is non-empty, so there is no reason to keep the
            # .rpmnew one created during this install.
            #
            rm -f /etc/.java/.systemPrefs/.systemRootModFile.rpmnew
        else
            #
            # The existing lock is empty, so replace it with the new one.  This
            # makes future installs a little cleaner, since the file in use is
            # the file in the RPM database.
            #
            rm -f /etc/.java/.systemPrefs/.systemRootModFile
            mv /etc/.java/.systemPrefs/.systemRootModFile.rpmnew \
               /etc/.java/.systemPrefs/.systemRootModFile
        fi
    fi

    #
    # Try to register the init script to the various run levels.  If possible
    # this is accomplished using an LSB defined install tool.  If that isn't
    # available, then try to use chkconfig, which is supported by Red Hat and
    # Debian.  The feature of automatic jar file execution is not support on
    # systems which don't support either of these interfaces.
    #
    if [ -x /usr/lib/lsb/install_initd ]; then
        /usr/lib/lsb/install_initd jexec > /dev/null 2>&1

        # start the service for the current session
        /etc/init.d/jexec start > /dev/null 2>&1
    elif [ -x /sbin/chkconfig ]; then
        /sbin/chkconfig --add jexec > /dev/null 2>&1

        # start the service for the current session
        /etc/init.d/jexec start > /dev/null 2>&1
    fi


%preun -p /bin/sh
#
    # Add the shell function and related variables used by the pre-uninstall.
    #
    MOST_DIGITS="[1-9]"
ALL_DIGITS="[0-9]"
COUNTING_NUMBER="${MOST_DIGITS}${ALL_DIGITS}*\|0"
VALID_NON_NUMERIC="[-_.a-zA-Z]"
VALID_CHARS="[-_.a-zA-Z0-9]"
MAJOR_RULE="\(${MOST_DIGITS}${ALL_DIGITS}*\)"
MINOR_RULE="\(${COUNTING_NUMBER}\)"
MICRO_RULE="\(${COUNTING_NUMBER}\)"
UPDATE_RULE="\(${MOST_DIGITS}${ALL_DIGITS}\|0${ALL_DIGITS}\)"
NON_FCS_ID_RULE="\([a-zA-Z0-9]*\)"
MIN_VERSION_ID_RULE="${MAJOR_RULE}\.${MINOR_RULE}\.${MICRO_RULE}"
FCS_VERSION_ID_RULE="${MIN_VERSION_ID_RULE}\(_${UPDATE_RULE}\)\?"
VERSION_ID_RULE="${FCS_VERSION_ID_RULE}\(-${NON_FCS_ID_RULE}\)\?"
NAME_ID_RULE="${VALID_CHARS}*${VALID_NON_NUMERIC}"
KNOWN_GOOD_NAME_LIST="java jdk jre j2sdk j2re"
PRS_ERROR_BAD_PARAMS=2000
expand_version() {
    status=0
    if [ $# -eq 0 ]; then
        read release remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${release}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${release}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        release=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        \printf "\t expand_version\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        format="%d\t%d\t%d\t%d\n"
        echo ${release} | sed -e "s/_/\./g" | \
          awk -v format="${format}" 'BEGIN { FS = "." } { printf format, $1, $2, $3, $4 }'
    fi
    return ${status}
}
parse_release() {
    status=0
    if [ $# -eq 0 ]; then
        read string remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${string}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${string}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        string=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t parse_release %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        version_id=`expr "${string}" : "${NAME_ID_RULE}\(${VERSION_ID_RULE}\)\$"`
        if [ -n "${version_id}" ]; then
            name_id=`expr "${string}" : "\(${NAME_ID_RULE}\)${VERSION_ID_RULE}\$"`
            fcs_part=`expr "${string}" : "${NAME_ID_RULE}\(${FCS_VERSION_ID_RULE}\).*\$"`
            non_fcs_part=`expr "${version_id}" : "[^-]*-\(${NON_FCS_ID_RULE}\)\$"`
	    printf "%s\t%s\t%s\n" "${name_id}" "${fcs_part}" "${non_fcs_part}"
        fi
    fi
    return ${status}
}
UNKNOWN_NAME_WEIGHT=1000
get_name_weight() {
    status=0
    if [ "$1" = "-" ]; then
        read name good_names
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        else
            shift 1
            if [ $# -gt 0 ]; then
                good_names="$*"
            fi
            if [ -z "${name}" ]; then
                printf "Error: usage - function requires input!\n" >> /dev/stderr
                status=${PRS_ERROR_BAD_PARAMS}
            fi
        fi
    elif [ $# -gt 1 ]; then
        name=$1
        shift 1
        good_names="$*"
    else
        printf "Error: usage - function takes 2+ parameters:\n\n" >> /dev/stderr
        printf "\t get_name_weight %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -n "${good_names}" ]; then
            length=`expr length "${good_names}"`
            pos=`expr "${good_names}" : ".*\<${name}\>"`
            if [ ${pos} -gt 0 ]; then
                expr substr "${good_names}" 1 ${pos} | wc -w | tr -d "[:space:]"
            else
                echo ${UNKNOWN_NAME_WEIGHT}
            fi
        else
            echo ${UNKNOWN_NAME_WEIGHT}
        fi
    fi
    return ${status}
}
HAS_FCS_WEIGHT=0
HAS_ODD_FCS_WEIGHT=1
HAS_RC_WEIGHT=100
HAS_ODD_RC_WEIGHT=101
HAS_BETA_WEIGHT=300
HAS_ODD_BETA_WEIGHT=301
HAS_EA_WEIGHT=500
HAS_ODD_EA_WEIGHT=501
HAS_INTRNAL_WEIGHT=2000
HAS_VERY_ODD_WEIGHT=9999
get_non_fcs_weight() {
    status=0
    if [ $# -eq 0 ]; then
        read non_fcs_part remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${non_fcs_part}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        non_fcs_part=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t get_non_fcs_weight \n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -z "${non_fcs_part}" ]; then
            echo ${HAS_FCS_WEIGHT}
        else
            case "${non_fcs_part}" in
                fcs)
                    echo ${HAS_ODD_FCS_WEIGHT}
                    ;;
                rc)
                    echo ${HAS_RC_WEIGHT}
                    ;;
                rc[0-9] | rc[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "rc\([0-9]*\)$"`
                    echo `expr ${HAS_RC_WEIGHT} - ${count}`
                    ;;
                rc*)
                    echo ${HAS_ODD_RC_WEIGHT}
                    ;;
                beta)
                    echo ${HAS_BETA_WEIGHT}
                    ;;
                beta[0-9] | beta[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "beta\([0-9]*\)$"`
                    echo `expr ${HAS_BETA_WEIGHT} - ${count}`
                    ;;
                beta*)
                    echo ${HAS_ODD_BETA_WEIGHT}
                    ;;
                ea)
                    echo ${HAS_EA_WEIGHT}
                    ;;
                ea[0-9] | ea[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "ea\([0-9]*\)$"`
                    echo `expr ${HAS_EA_WEIGHT} - ${count}`
                    ;;
                ea*)
                    echo ${HAS_ODD_EA_WEIGHT}
                    ;;
                internal)
                    echo ${HAS_INTRNAL_WEIGHT}
                    ;;
                internal[0-9] | internal[0-9][0-9] | internal[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "internal\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                b[0-9] | b[0-9][0-9] | b[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "b\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                *)
                    echo ${HAS_VERY_ODD_WEIGHT}
                    ;;
            esac
        fi
    fi
    return ${status}
}
    get_path_weight() {
    good_list="$1"
    path=$2
    release=`basename ${path}`
    parts="`parse_release ${release}`"
    if [ $? -eq 0 ]; then
        name=`echo "${parts}" | cut -f1`
        version=`echo "${parts}" | cut -f2`
        non_fcs=`echo "${parts}" | cut -f3`
        if [ -n "${version}" ]; then
           v_weight=`echo ${version} | expand_version`
           n_weight=`echo ${name} | get_name_weight - "${good_list}"`
           o_weight=`echo ${non_fcs} | get_non_fcs_weight`
           printf "%4d  %4d  %4d  %4d  %4d  %4d  %s\n" \
                  ${v_weight} ${n_weight} ${o_weight} "${path}"
        fi
    fi
}
get_weighted_list() {
    good_list=
    verify=
    stdio=
    status=0
    check=true
    while [ -n "${check}" ]; do
        if [ $# -gt 0 ]; then
            case "$1" in
                -g)
                    good_list="$2"
                    shift 2
                    ;;
                --good-list=*)
                    length=`expr length "$1"`
                    remove=`expr \( length "--good-list=" \) + 1`
                    good_list="`expr substr \"$1\" ${remove} ${length}`"
                    shift 1
                    ;;
                -v | --verify)
                    verify=true
                    shift 1
                    ;;
                --)
                    shift 1
                    check=
                    ;;
                -)
                    shift 1
                    stdio=true
                    ;;
                -*)
                    printf "Error: usage - unknown parameter:\n\n" \
								>> /dev/stderr
                    printf "\t%s : %s\n" "$1" "$*"		>> /dev/stderr
                    status=${PRS_ERROR_BAD_PARAMS}
                    check=
                    ;;
                *)
                    check=
                    ;;
            esac
        else
            check=
        fi
    done
    if [ $# -eq 0 ] || [ -n "${stdio}" ]; then
        read line
        while [ -n "${line}" ]; do
            if [ -z "${verify}" ] || [ -f ${line}/bin/java ]; then
                get_path_weight "${good_list}" ${line}
            fi
            read line
        done
    fi
    while [ $# -gt 0 ]; do
        if [ -z "${verify}" ] || [ -f $1/bin/java ]; then
            get_path_weight "${good_list}" $1
        fi
        shift 1
    done
    return ${status}
}
_compare_java_by_weight() {
    compare=0
    if [ $# -ne 0 ]; then
        if [ $# -eq 1 ]; then
            compare=1
        else
            left=$1
            right=$2
            shift 2
            good="$*"
            list=`get_weighted_list --good-list="${good}" \
                    ${left} ${right} | sort -u -k1n -k2n -k3n -k4n -k5rn -k6rn`
            if [ `echo "${list}" | wc -l | tr -d "[:space:]"` -ne 1 ]; then
                compare=-1
                latest=`echo "${list}" | tail -n 1 | cut -c 37-`
                if [ "${left}" = "${latest}" ]; then
                    compare=1
                fi
            fi
        fi
    fi
    echo ${compare}
}
compare_java_by_version() {
    _compare_java_by_weight $1 $2
}
compare_java_by_release() {
    _compare_java_by_weight $1 $2 ${KNOWN_GOOD_NAME_LIST}
}
find_latest_release() {
    if [ -d /usr/java ]; then
        latest_release=`find /usr/java/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
    fi
    if [ -d "${RPM_INSTALL_PREFIX}" ] && \
       [ "/usr/java" != "${RPM_INSTALL_PREFIX}" ]
    then 
        prefix_release=`find ${RPM_INSTALL_PREFIX}/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
        if [ `compare_java_by_release ${latest_release} ${prefix_release}` -lt 0 ]; then
            latest_release=${prefix_release}
        fi
    fi
    echo ${latest_release}
}
get_javaws() {
    path=$1
    if [ `compare_java_by_version ${path} version-1.5.0` -ge 0 ] &&
       [ -f ${path}/bin/javaws ]
    then
        path=${path}/bin/javaws
    elif [ `compare_java_by_version ${path} version-1.4.2` -ge 0 ]; then
        if [ -f ${path}/jre/javaws/javaws ]; then
            path=${path}/jre/javaws/javaws
        elif [ -f ${path}/javaws/javaws ]; then
            path=${path}/javaws/javaws
        else
            path=
        fi
    else
        path=
    fi
    echo ${path}
}
    LINK_ERROR_BAD_PARAMS=3000
LINK_ERROR_DEAD_LINK=3001
LINK_ERROR_FILE_NOT_FOUND=3002
dereference() {
    status=0
    if [ "$1" = "-f" ] || [ "$1" = "--follow" ]; then
        follow="--follow"
        shift 1
    fi
    if [ $# -ge 1 ]; then
        path="$*"
        if [ -e "${path}" ]; then
            parent="`cd \`dirname \"${path}\"\`; pwd`"
            child="`basename \"${path}\"`"
            if [ "${parent}" != "${child}" ]; then
                path="${parent}/${child}"
            fi
            if [ -h "${path}" ]; then
                path=`ls -l "${path}" | sed -e "s#^.*${path} -> ##"`
                if [ "`expr substr \"${path}\" 1 1`" != "/" ]; then
                    path="${parent}/${path}"
                fi
                if [ -n "${follow}" ]; then
                    path="`dereference ${follow} ${path}`"
                fi                    
            fi
        else
            status=${LINK_ERROR_FILE_NOT_FOUND}
        fi
    fi
    echo ${path}
    return ${status}
}
setup_latest_link() {
    latest=$1
    link=$2
    if [ -h "${link}" ]; then
        reference="`dereference --follow ${link}`"
        if [ $? -eq 0 ]; then
            update=`compare_java_by_release "${latest}" "${reference}"`
        else
            update=1
        fi
        if [ ${update} -gt 0 ]; then
            rm -f "${link}"
        fi
    fi
    if [ ! -e "${link}" ]; then
        ln -s "${latest}" "${link}"
    fi
}
setup_default_links() {
    if [ $# -ge 2 ]; then
        latest_link="$1"
        default_link="$2"
        if [ ! -e "${default_link}" ]; then
            ln -s "${latest_link}" "${default_link}"
        fi
    fi
    if [ $# -gt 3 ]; then
        bindir="$3"
        shift 3
        for file in $*; do
            reference="`dereference --follow ${bindir}/${file}`"
            if [ $? -ne 0 ]; then
                rm -f "${bindir}/${file}"
            fi
            source="${default_link}/bin/${file}"
            if [ "${file}" = "javaws" ]; then
                source="`get_javaws \"${default_link}\"`"
            fi
            if [ -n "${source}" ] && [ ! -e "${bindir}/${file}" ]; then
                ln -s "${source}" "${bindir}/${file}"
            fi
        done
    fi
}
cleanup_default_links() {
    if [ $# -ge 1 ]; then
        default_link=$1
        if [ $# -gt 2 ]; then
            bindir="$2"
            shift 2
            for file in $*; do
                reference="`dereference \"${bindir}/${file}\"`"
                if [ $? -ne 0 ] ||
                   [ "${reference}" = "${default_link}/bin/${file}" ]
                then
                    rm -f "${bindir}/${file}"
                fi
            done
        fi
        rm -f "${default_link}"
    fi
}


    #
    # Dereference and follow any links that might have been created when this
    # package was installed.  If a link ultimately points to this installation
    # or the link is dead, then we should remove the link.  Important links,
    # like default and latest can be remade in post-uninstall (%postun).
    #
    # This is done in the reverse order the links were initially created in, in
    # case there are any partial loops.
    #
    if [ -h "/usr/java/default" ]; then
        DEFAULT_LINK="`dereference --follow \"/usr/java/default\"`"
        if [ $? -ne 0 ] ||
           [ "${DEFAULT_LINK}" = "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ]
        then
            cleanup_default_links "/usr/java/default" \
                                  "/usr/bin" java javaws jcontrol javac jar javadoc
        fi
    fi

    #
    # If the latest link still points to this installation it must mean one of
    # the following:
    #
    #     * No newer version of Java has been installed.  This is known because
    #       any such version would have already changed the latest to point
    #       to itself.
    #
    #     * No older version is installed.  We don't check this now, but if this
    #       is the case, now is the best time to remove the latest link, since
    #       anything pointing to this installation in post-uninstall will be a
    #       dead link.
    #
    #     * There is an older version of Java installed.  In this case we need
    #       to handle the latest link differently depending on what version
    #       remains.
    #
    if [ -h "/usr/java/latest" ]; then
        LATEST_LINK="`dereference --follow \"/usr/java/latest\"`"
        if [ $? -ne 0 ] ||
           [ "${LATEST_LINK}" = "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ]
        then
            #
            # If this version is the latest, and the first version with jexec
            # support, then stop and remove the jexec service.  If this isn't
            # done now, there might not be an init script left when %postun is
            # called, and if there is, we can restart/reinstall the service
            # easy enough then.
            #
            if [ `compare_java_by_version ${LATEST_LINK} \
                                  version-1.6.0` -ge 0 ] &&
               [ -x /etc/init.d/jexec ]
            then
                /etc/init.d/jexec stop > /dev/null 2>&1

                if [ -x /usr/lib/lsb/remove_initd ]; then
                    /usr/lib/lsb/remove_initd jexec > /dev/null 2>&1
                elif [ -x /sbin/chkconfig ]; then
                    /sbin/chkconfig --del jexec > /dev/null 2>&1
                fi
            fi

            rm -f "/usr/java/latest" 2> /dev/null
        fi
    fi

    #
    # If the package was relocated when it was installed, there should be a link
    # in /usr/java.  So, if there is a link named /usr/java/jdk1.6.0_45 that is
    # dead, or points back to ${RPM_INSTALL_PREFIX}, delete it.
    #
    if [ "${RPM_INSTALL_PREFIX}" != "/usr/java" ] &&
       [ -h "/usr/java/jdk1.6.0_45" ]
    then
        THIS_LINK="`dereference --follow \"/usr/java/jdk1.6.0_45\"`"
        if [ $? -ne 0 ] ||
           [ "${THIS_LINK}" = "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ]
        then
            rm -f "/usr/java/jdk1.6.0_45" 2> /dev/null
        fi
    fi


%postun -p /bin/sh
#
    # Make sure any new files are created with a secure access mask.  Do not use
    # chmod, since that would also change the rights of any existing files, and
    # we are only interested in setting the rights for new files.
    #
    umask 022

    #
    # The package assumes that Gnome is either installed, or going to be
    # installed, so if nothing currently exists, then install in the default
    # location.
    #
    # NOTE: These variables must be defined before all the shell function macros
    #       are included.
    #
    if [ -z "${GNOMEDIR}" ]; then
        GNOMEDIR=/usr
    fi

    #
    # RPM_INSTALL_PREFIX doesn't seem to be set by "alien" so the following
    # minor kludge allows some functionality on debian-like systems (such
    # a Ubuntu) which don't support packages.
    #
    if [ -z "${RPM_INSTALL_PREFIX}" ]; then
	RPM_INSTALL_PREFIX="/usr/java"
    fi

    #
    # Gross kludge for old SuSE distros: Even though they set the environment
    # variable GNOMEDIR to /opt/gnome, Gnome may really be in /opt/gnome2.
    # Go figure,... (I feel so unclean....)
    #
    if [ "${GNOMEDIR}" = "/opt/gnome" ] && [ -d "/opt/gnome2" ]; then
	GNOMEDIR="/opt/gnome2"
    fi

    INSTALL_JRE_PATH=${RPM_INSTALL_PREFIX}/jdk1.6.0_45
    if [ -e ${INSTALL_JRE_PATH}/jre/bin/java ]; then
	INSTALL_JRE_PATH=${INSTALL_JRE_PATH}/jre
    fi

    #
    # Add the shell function and related variables used by the post-uninstall.
    #
    NS_COMMENT1="#--Netscape Communications Corporation MIME Information"
NS_COMMENT2="#Do not delete the above line. It is used to identify the file type."
NS_COMMENT3="#mime types added by Netscape Helper"
UpdateMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    command="$3"
    if [ -z "`grep -E \"^${mime_type}; ${command}$\" \"${mailcap_file}\" 2> /dev/null`" ]; then
        mc_comment="# Java Web Start"
        mc_text=
        if [ -w "${mailcap_file}" ]; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
        fi
        if [ -w "`dirname \"${mailcap_file}\"`" ]; then
            mc_text="${mc_text:+${mc_text}\n}${mime_type}; ${command}"
            printf "%s" "${mc_text}" > "${mailcap_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mailcap_file}"
            echo "Check permissions."
        fi
    fi
}
RemoveMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    mc_comment="# Java Web Start"
    if [ -w "${mailcap_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mailcap_file}\"`" ] ; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
            if [ `echo "${mc_text}" | tr -d '[:space:]' | wc -c` -gt 0 ]; then
                echo "${mc_text}" > "${mailcap_file}"
            else
                rm -f "${mailcap_file}"
            fi
        fi
    fi
}
UpdateMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    desc="$3"
    shift 3
    exts="$*"
    JNLP_ENTRY="type=${mime_type} desc=\"${desc}\" exts=\"${exts}\""
    if [ ! -w "${mime_file}" ]; then
        if [ -w `dirname ${mime_file}` ]; then
            echo "${NS_COMMENT1}"  > "${mime_file}"
            echo "${NS_COMMENT2}" >> "${mime_file}"
            echo "${NS_COMMENT3}" >> "${mime_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mime_file}"
            echo "Check permissions."
            return
        fi
    fi
    if [ -z "`grep -E \"^[^#]*${mime_type}\" \"${mime_file}\"`" ]; then
        echo ${JNLP_ENTRY} >> "${mime_file}"
    fi
}
RemoveMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    if [ -w "${mime_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mime_file}\"`" ]; then
            regexp="(${mime_type})|(^${NS_COMMENT1}$)|(^${NS_COMMENT2}$)|(^${NS_COMMENT3}$)"
            if [ `grep -Ev "${regexp}" "${mime_file}" | \
                 tr -d '[:space:]' | wc -c` -gt 0 ]
            then
                mt_text="`grep -v \"${mime_type}\" \"${mime_file}\"`"
                echo "${mt_text}" > "${mime_file}"
            else
                rm -f "${mime_file}"
            fi
        fi
    fi
}
    JDK_DESKTOP="${INSTALL_JRE_PATH}/lib/desktop"
JDK_ICONS="${JDK_DESKTOP}/icons"
JDK_APPS="${JDK_DESKTOP}/applications"
JDK_MIME="${JDK_DESKTOP}/mime"
SHARE_PATH="${GNOMEDIR}/share"
SHARE_ICONS="${SHARE_PATH}/icons"
SHARE_MIME="${SHARE_PATH}/mime"
SHARE_APPS="${SHARE_PATH}/applications"
HICOLOR=hicolor
HIGHCONTRAST=HighContrast
HIGHCONTRASTINVERSE=HighContrastInverse
LOWCONTRAST=LowContrast
THEMES="${HICOLOR} ${HIGHCONTRAST} ${HIGHCONTRASTINVERSE} ${LOWCONTRAST}"
RESOLUTIONS="16x16 48x48"
TEXT_ICON="gnome-mime-text-x-java.png"
JAR_ICON="gnome-mime-application-x-java-archive.png"
JNLP_ICON="gnome-mime-application-x-java-jnlp-file.png"
JAVA_ICON="sun-java.png"
JAVAWS_ICON="sun-javaws.png"
JCONTROL_ICON="sun-jcontrol.png"
APPS_ICONS="${JAVA_ICON} ${JAVAWS_ICON} ${JCONTROL_ICON}"
MIME_ICONS="${TEXT_ICON} ${JAR_ICON} ${JNLP_ICON}"
ICONS="${APPS_ICONS} ${MIME_ICONS}"
GNOME_UTILS_DIRS="/usr/bin /opt/gnome/bin"
UPDATE_MIME_DATABASE="update-mime-database"
UPDATE_DESKTOP_DATABASE="update-desktop-database"
GTK_UPDATE_ICON_CACHE="gtk-update-icon-cache"
SHARE_CONTROL_CENTER="${SHARE_PATH}/control-center-2.0"
SHARE_CAPPLETS="${SHARE_CONTROL_CENTER}/capplets"
SHARE_MIME_INFO="${SHARE_PATH}/mime-info"
SHARE_APP_REGISTRY="${SHARE_PATH}/application-registry"
SHARE_PIXMAPS="${SHARE_PATH}/pixmaps"
UpdateIconCache() {
    _icon_theme_root=$1
    if [ -f ${_icon_theme_root}/icon-theme.cache ]; then
	for _dir in ${GNOME_UTILS_DIRS}; do
	    if [ -x ${_dir}/${GTK_UPDATE_ICON_CACHE} ]; then
		${_dir}/${GTK_UPDATE_ICON_CACHE} ${_icon_theme_root} \
		    > /dev/null 2>&1
		break
	    fi
	done
	touch ${_icon_theme_root}
	for _dir in ${RESOLUTIONS}; do
	    if [ -d ${_icon_theme_root}/${_dir} ]; then
		touch ${_icon_theme_root}/${_dir}
	    fi
        done
    fi
}
UpdateDesktopDatabase() {
    _desktop_root=$1
    if [ -f ${_desktop_root}/mimeinfo.cache ]; then
	for _dir in ${GNOME_UTILS_DIRS}; do
	    if [ -x ${_dir}/${UPDATE_DESKTOP_DATABASE} ]; then
		${_dir}/${UPDATE_DESKTOP_DATABASE} ${_desktop_root} \
		   > /dev/null 2>&1
		break
	    fi
	done
    fi
}
UpdateMimeDatabase() {
    _mime_root=$1
    if [ -d ${_mime_root}/packages ]; then
	for _dir in ${GNOME_UTILS_DIRS}; do
	    if [ -x ${_dir}/${UPDATE_MIME_DATABASE} ]; then
		${_dir}/${UPDATE_MIME_DATABASE} ${_mime_root} > /dev/null 2>&1
		break
	    fi
	done
    fi
}
InstallGnomeIcons() {
    for _theme in ${THEMES}; do
	if [ -d ${SHARE_ICONS}/${_theme} ]; then
	    for _res in ${RESOLUTIONS}; do
		mkdir -p ${SHARE_ICONS}/${_theme}/${_res}/apps
		for _icon in ${APPS_ICONS}; do
		    cp -f ${JDK_ICONS}/${_theme}/${_res}/apps/${_icon} \
			  ${SHARE_ICONS}/${_theme}/${_res}/apps/${_icon}
		done
		mkdir -p ${SHARE_ICONS}/${_theme}/${_res}/mimetypes
		for _icon in ${MIME_ICONS}; do
		    cp -f ${JDK_ICONS}/${_theme}/${_res}/mimetypes/${_icon} \
			  ${SHARE_ICONS}/${_theme}/${_res}/mimetypes/${_icon}
		done
	    done
	    UpdateIconCache ${SHARE_ICONS}/${_theme}
	fi
    done
    if [ -d ${SHARE_PIXMAPS} ]; then
	for _icon in ${APPS_ICONS}; do
	    cp -f ${JDK_ICONS}/${HICOLOR}/48x48/apps/${_icon} \
		  ${SHARE_PIXMAPS}/${_icon}
	done
	cp -f ${JDK_ICONS}/${HICOLOR}/48x48/mimetypes/${TEXT_ICON} \
	      ${SHARE_PIXMAPS}/x-java.png
	cp -f ${JDK_ICONS}/${HICOLOR}/48x48/mimetypes/${JAR_ICON} \
	      ${SHARE_PIXMAPS}/x-java-archive.png
	cp -f ${JDK_ICONS}/${HICOLOR}/48x48/mimetypes/${JNLP_ICON} \
	      ${SHARE_PIXMAPS}/x-java-jnlp-file.png
    fi
}
RemoveGnomeIcons() {
    for _theme in ${THEMES}; do
	for _res in ${RESOLUTIONS}; do
	    for _icon in ${APPS_ICONS}; do
		rm -f ${SHARE_ICONS}/${_theme}/${_res}/apps/${_icon}
	    done
	    for _icon in ${MIME_ICONS}; do
		rm -f ${SHARE_ICONS}/${_theme}/${_res}/mimetypes/${_icon}
	    done
	done
	UpdateIconCache ${SHARE_ICONS}/${_theme}
    done
    if [ -d ${SHARE_PIXMAPS} ]; then
	for _icon in ${APPS_ICONS}; do
	    rm -f ${SHARE_PIXMAPS}/${_icon}
	done
	rm -f ${SHARE_PIXMAPS}/x-java.png
	rm -f ${SHARE_PIXMAPS}/x-java-archive.png
	rm -f ${SHARE_PIXMAPS}/x-java-jnlp-file.png
    fi
}
InstallGnomeDesktop() {
    _file=$1
    mkdir -p ${SHARE_APPS}
    cp -f ${JDK_APPS}/${_file} ${SHARE_APPS}/${_file}
    if [ "${_file}" = "sun_java.desktop" ]; then
	if [ -d ${SHARE_CAPPLETS} ]; then
	    cp -f ${JDK_APPS}/${_file} ${SHARE_CAPPLETS}/${_file}
	fi
    fi
}
RemoveGnomeDesktop() {
    _file=$1
    rm -f ${SHARE_APPS}/${_file}
    rm -f ${SHARE_CAPPLETS}/${_file}
}
InstallLegacyMimetype() {
    _mime_type=$1
    _extension=$2
    _name=$3
    _command=$4
    _icon=$5
    _description=$6
    cat <<- end_of_keys_file > ${SHARE_MIME_INFO}/${_name}.keys
	${_mime_type}:
	    description=${_description}
	    icon_filename=${_icon}
	    default_action_type=application
	    default_application_id=${_name}
	    short_list_application_user_additions=${_name}
	end_of_keys_file
    cat <<- end_of_mime_file > ${SHARE_MIME_INFO}/${_name}.mime
	${_mime_type}
	    ext: ${_extension}
	end_of_mime_file
    cat <<- end_of_apps_file > ${SHARE_APP_REGISTRY}/${_name}.applications
	${_name}
	    command=${_command}
	    name=${_name}
	    can_open_multiple_files=false
	    requires_terminal=false
	    mime_types=${_mime_type}
	end_of_apps_file
}
RemoveLegacyMimetype() {
    _name=$1
    rm -f ${SHARE_MIME_INFO}/${_name}.keys
    rm -f ${SHARE_MIME_INFO}/${_name}.mime
    rm -f ${SHARE_APP_REGISTRY}/${_name}.applications
}
InstallGnomeMimetypes() {
    if [ -d ${SHARE_MIME} ]; then
	cp -f ${JDK_MIME}/packages/x-java-archive.xml \
	      ${SHARE_MIME}/packages/x-java-archive.xml
	cp -f ${JDK_MIME}/packages/x-java-jnlp-file.xml \
	      ${SHARE_MIME}/packages/x-java-jnlp-file.xml
    fi
    UpdateMimeDatabase ${SHARE_MIME}
    if [ -d ${SHARE_MIME_INFO} ] || [ -d ${SHARE_APP_REGISTRY} ]; then
	mkdir -p ${SHARE_MIME_INFO}
	mkdir -p ${SHARE_APP_REGISTRY}
	InstallLegacyMimetype application/x-java-archive \
                 jar              \
                 java-archive     \
                 "java -jar"      \
                 x-java-archive.png     \
		 "Java Archive"
	InstallLegacyMimetype application/x-java-jnlp-file \
                 jnlp                \
                 java-web-start      \
                 javaws              \
                 x-java-jnlp-file.png        \
                 "Java Web Start Application"
    fi
}
RemoveGnomeMimetypes() {
    rm -f ${SHARE_MIME}/packages/x-java-archive.xml
    rm -f ${SHARE_MIME}/packages/x-java-jnlp-file.xml
    UpdateMimeDatabase ${SHARE_MIME}
    if [ -d ${SHARE_MIME_INFO} ] || [ -d ${SHARE_APP_REGISTRY} ]; then
	RemoveLegacyMimetype java-archive
	RemoveLegacyMimetype java-web-start
    fi
}
IntegrateWithGnome() {
    InstallGnomeIcons
    InstallGnomeDesktop sun_java.desktop
    InstallGnomeDesktop sun-java.desktop
    InstallGnomeDesktop sun-javaws.desktop
    UpdateDesktopDatabase ${SHARE_APPS}
    InstallGnomeMimetypes
}
DisintegrateWithGnome() {
    RemoveGnomeIcons
    RemoveGnomeDesktop sun_java.desktop
    RemoveGnomeDesktop sun-java.desktop
    RemoveGnomeDesktop sun-javaws.desktop
    UpdateDesktopDatabase ${SHARE_APPS}
    RemoveGnomeMimetypes
}
    MOST_DIGITS="[1-9]"
ALL_DIGITS="[0-9]"
COUNTING_NUMBER="${MOST_DIGITS}${ALL_DIGITS}*\|0"
VALID_NON_NUMERIC="[-_.a-zA-Z]"
VALID_CHARS="[-_.a-zA-Z0-9]"
MAJOR_RULE="\(${MOST_DIGITS}${ALL_DIGITS}*\)"
MINOR_RULE="\(${COUNTING_NUMBER}\)"
MICRO_RULE="\(${COUNTING_NUMBER}\)"
UPDATE_RULE="\(${MOST_DIGITS}${ALL_DIGITS}\|0${ALL_DIGITS}\)"
NON_FCS_ID_RULE="\([a-zA-Z0-9]*\)"
MIN_VERSION_ID_RULE="${MAJOR_RULE}\.${MINOR_RULE}\.${MICRO_RULE}"
FCS_VERSION_ID_RULE="${MIN_VERSION_ID_RULE}\(_${UPDATE_RULE}\)\?"
VERSION_ID_RULE="${FCS_VERSION_ID_RULE}\(-${NON_FCS_ID_RULE}\)\?"
NAME_ID_RULE="${VALID_CHARS}*${VALID_NON_NUMERIC}"
KNOWN_GOOD_NAME_LIST="java jdk jre j2sdk j2re"
PRS_ERROR_BAD_PARAMS=2000
expand_version() {
    status=0
    if [ $# -eq 0 ]; then
        read release remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${release}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${release}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        release=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        \printf "\t expand_version\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        format="%d\t%d\t%d\t%d\n"
        echo ${release} | sed -e "s/_/\./g" | \
          awk -v format="${format}" 'BEGIN { FS = "." } { printf format, $1, $2, $3, $4 }'
    fi
    return ${status}
}
parse_release() {
    status=0
    if [ $# -eq 0 ]; then
        read string remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${string}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${string}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        string=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t parse_release %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        version_id=`expr "${string}" : "${NAME_ID_RULE}\(${VERSION_ID_RULE}\)\$"`
        if [ -n "${version_id}" ]; then
            name_id=`expr "${string}" : "\(${NAME_ID_RULE}\)${VERSION_ID_RULE}\$"`
            fcs_part=`expr "${string}" : "${NAME_ID_RULE}\(${FCS_VERSION_ID_RULE}\).*\$"`
            non_fcs_part=`expr "${version_id}" : "[^-]*-\(${NON_FCS_ID_RULE}\)\$"`
	    printf "%s\t%s\t%s\n" "${name_id}" "${fcs_part}" "${non_fcs_part}"
        fi
    fi
    return ${status}
}
UNKNOWN_NAME_WEIGHT=1000
get_name_weight() {
    status=0
    if [ "$1" = "-" ]; then
        read name good_names
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        else
            shift 1
            if [ $# -gt 0 ]; then
                good_names="$*"
            fi
            if [ -z "${name}" ]; then
                printf "Error: usage - function requires input!\n" >> /dev/stderr
                status=${PRS_ERROR_BAD_PARAMS}
            fi
        fi
    elif [ $# -gt 1 ]; then
        name=$1
        shift 1
        good_names="$*"
    else
        printf "Error: usage - function takes 2+ parameters:\n\n" >> /dev/stderr
        printf "\t get_name_weight %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -n "${good_names}" ]; then
            length=`expr length "${good_names}"`
            pos=`expr "${good_names}" : ".*\<${name}\>"`
            if [ ${pos} -gt 0 ]; then
                expr substr "${good_names}" 1 ${pos} | wc -w | tr -d "[:space:]"
            else
                echo ${UNKNOWN_NAME_WEIGHT}
            fi
        else
            echo ${UNKNOWN_NAME_WEIGHT}
        fi
    fi
    return ${status}
}
HAS_FCS_WEIGHT=0
HAS_ODD_FCS_WEIGHT=1
HAS_RC_WEIGHT=100
HAS_ODD_RC_WEIGHT=101
HAS_BETA_WEIGHT=300
HAS_ODD_BETA_WEIGHT=301
HAS_EA_WEIGHT=500
HAS_ODD_EA_WEIGHT=501
HAS_INTRNAL_WEIGHT=2000
HAS_VERY_ODD_WEIGHT=9999
get_non_fcs_weight() {
    status=0
    if [ $# -eq 0 ]; then
        read non_fcs_part remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${non_fcs_part}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        non_fcs_part=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t get_non_fcs_weight \n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -z "${non_fcs_part}" ]; then
            echo ${HAS_FCS_WEIGHT}
        else
            case "${non_fcs_part}" in
                fcs)
                    echo ${HAS_ODD_FCS_WEIGHT}
                    ;;
                rc)
                    echo ${HAS_RC_WEIGHT}
                    ;;
                rc[0-9] | rc[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "rc\([0-9]*\)$"`
                    echo `expr ${HAS_RC_WEIGHT} - ${count}`
                    ;;
                rc*)
                    echo ${HAS_ODD_RC_WEIGHT}
                    ;;
                beta)
                    echo ${HAS_BETA_WEIGHT}
                    ;;
                beta[0-9] | beta[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "beta\([0-9]*\)$"`
                    echo `expr ${HAS_BETA_WEIGHT} - ${count}`
                    ;;
                beta*)
                    echo ${HAS_ODD_BETA_WEIGHT}
                    ;;
                ea)
                    echo ${HAS_EA_WEIGHT}
                    ;;
                ea[0-9] | ea[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "ea\([0-9]*\)$"`
                    echo `expr ${HAS_EA_WEIGHT} - ${count}`
                    ;;
                ea*)
                    echo ${HAS_ODD_EA_WEIGHT}
                    ;;
                internal)
                    echo ${HAS_INTRNAL_WEIGHT}
                    ;;
                internal[0-9] | internal[0-9][0-9] | internal[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "internal\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                b[0-9] | b[0-9][0-9] | b[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "b\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                *)
                    echo ${HAS_VERY_ODD_WEIGHT}
                    ;;
            esac
        fi
    fi
    return ${status}
}
    get_path_weight() {
    good_list="$1"
    path=$2
    release=`basename ${path}`
    parts="`parse_release ${release}`"
    if [ $? -eq 0 ]; then
        name=`echo "${parts}" | cut -f1`
        version=`echo "${parts}" | cut -f2`
        non_fcs=`echo "${parts}" | cut -f3`
        if [ -n "${version}" ]; then
           v_weight=`echo ${version} | expand_version`
           n_weight=`echo ${name} | get_name_weight - "${good_list}"`
           o_weight=`echo ${non_fcs} | get_non_fcs_weight`
           printf "%4d  %4d  %4d  %4d  %4d  %4d  %s\n" \
                  ${v_weight} ${n_weight} ${o_weight} "${path}"
        fi
    fi
}
get_weighted_list() {
    good_list=
    verify=
    stdio=
    status=0
    check=true
    while [ -n "${check}" ]; do
        if [ $# -gt 0 ]; then
            case "$1" in
                -g)
                    good_list="$2"
                    shift 2
                    ;;
                --good-list=*)
                    length=`expr length "$1"`
                    remove=`expr \( length "--good-list=" \) + 1`
                    good_list="`expr substr \"$1\" ${remove} ${length}`"
                    shift 1
                    ;;
                -v | --verify)
                    verify=true
                    shift 1
                    ;;
                --)
                    shift 1
                    check=
                    ;;
                -)
                    shift 1
                    stdio=true
                    ;;
                -*)
                    printf "Error: usage - unknown parameter:\n\n" \
								>> /dev/stderr
                    printf "\t%s : %s\n" "$1" "$*"		>> /dev/stderr
                    status=${PRS_ERROR_BAD_PARAMS}
                    check=
                    ;;
                *)
                    check=
                    ;;
            esac
        else
            check=
        fi
    done
    if [ $# -eq 0 ] || [ -n "${stdio}" ]; then
        read line
        while [ -n "${line}" ]; do
            if [ -z "${verify}" ] || [ -f ${line}/bin/java ]; then
                get_path_weight "${good_list}" ${line}
            fi
            read line
        done
    fi
    while [ $# -gt 0 ]; do
        if [ -z "${verify}" ] || [ -f $1/bin/java ]; then
            get_path_weight "${good_list}" $1
        fi
        shift 1
    done
    return ${status}
}
_compare_java_by_weight() {
    compare=0
    if [ $# -ne 0 ]; then
        if [ $# -eq 1 ]; then
            compare=1
        else
            left=$1
            right=$2
            shift 2
            good="$*"
            list=`get_weighted_list --good-list="${good}" \
                    ${left} ${right} | sort -u -k1n -k2n -k3n -k4n -k5rn -k6rn`
            if [ `echo "${list}" | wc -l | tr -d "[:space:]"` -ne 1 ]; then
                compare=-1
                latest=`echo "${list}" | tail -n 1 | cut -c 37-`
                if [ "${left}" = "${latest}" ]; then
                    compare=1
                fi
            fi
        fi
    fi
    echo ${compare}
}
compare_java_by_version() {
    _compare_java_by_weight $1 $2
}
compare_java_by_release() {
    _compare_java_by_weight $1 $2 ${KNOWN_GOOD_NAME_LIST}
}
find_latest_release() {
    if [ -d /usr/java ]; then
        latest_release=`find /usr/java/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
    fi
    if [ -d "${RPM_INSTALL_PREFIX}" ] && \
       [ "/usr/java" != "${RPM_INSTALL_PREFIX}" ]
    then 
        prefix_release=`find ${RPM_INSTALL_PREFIX}/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
        if [ `compare_java_by_release ${latest_release} ${prefix_release}` -lt 0 ]; then
            latest_release=${prefix_release}
        fi
    fi
    echo ${latest_release}
}
get_javaws() {
    path=$1
    if [ `compare_java_by_version ${path} version-1.5.0` -ge 0 ] &&
       [ -f ${path}/bin/javaws ]
    then
        path=${path}/bin/javaws
    elif [ `compare_java_by_version ${path} version-1.4.2` -ge 0 ]; then
        if [ -f ${path}/jre/javaws/javaws ]; then
            path=${path}/jre/javaws/javaws
        elif [ -f ${path}/javaws/javaws ]; then
            path=${path}/javaws/javaws
        else
            path=
        fi
    else
        path=
    fi
    echo ${path}
}
    LINK_ERROR_BAD_PARAMS=3000
LINK_ERROR_DEAD_LINK=3001
LINK_ERROR_FILE_NOT_FOUND=3002
dereference() {
    status=0
    if [ "$1" = "-f" ] || [ "$1" = "--follow" ]; then
        follow="--follow"
        shift 1
    fi
    if [ $# -ge 1 ]; then
        path="$*"
        if [ -e "${path}" ]; then
            parent="`cd \`dirname \"${path}\"\`; pwd`"
            child="`basename \"${path}\"`"
            if [ "${parent}" != "${child}" ]; then
                path="${parent}/${child}"
            fi
            if [ -h "${path}" ]; then
                path=`ls -l "${path}" | sed -e "s#^.*${path} -> ##"`
                if [ "`expr substr \"${path}\" 1 1`" != "/" ]; then
                    path="${parent}/${path}"
                fi
                if [ -n "${follow}" ]; then
                    path="`dereference ${follow} ${path}`"
                fi                    
            fi
        else
            status=${LINK_ERROR_FILE_NOT_FOUND}
        fi
    fi
    echo ${path}
    return ${status}
}
setup_latest_link() {
    latest=$1
    link=$2
    if [ -h "${link}" ]; then
        reference="`dereference --follow ${link}`"
        if [ $? -eq 0 ]; then
            update=`compare_java_by_release "${latest}" "${reference}"`
        else
            update=1
        fi
        if [ ${update} -gt 0 ]; then
            rm -f "${link}"
        fi
    fi
    if [ ! -e "${link}" ]; then
        ln -s "${latest}" "${link}"
    fi
}
setup_default_links() {
    if [ $# -ge 2 ]; then
        latest_link="$1"
        default_link="$2"
        if [ ! -e "${default_link}" ]; then
            ln -s "${latest_link}" "${default_link}"
        fi
    fi
    if [ $# -gt 3 ]; then
        bindir="$3"
        shift 3
        for file in $*; do
            reference="`dereference --follow ${bindir}/${file}`"
            if [ $? -ne 0 ]; then
                rm -f "${bindir}/${file}"
            fi
            source="${default_link}/bin/${file}"
            if [ "${file}" = "javaws" ]; then
                source="`get_javaws \"${default_link}\"`"
            fi
            if [ -n "${source}" ] && [ ! -e "${bindir}/${file}" ]; then
                ln -s "${source}" "${bindir}/${file}"
            fi
        done
    fi
}
cleanup_default_links() {
    if [ $# -ge 1 ]; then
        default_link=$1
        if [ $# -gt 2 ]; then
            bindir="$2"
            shift 2
            for file in $*; do
                reference="`dereference \"${bindir}/${file}\"`"
                if [ $? -ne 0 ] ||
                   [ "${reference}" = "${default_link}/bin/${file}" ]
                then
                    rm -f "${bindir}/${file}"
                fi
            done
        fi
        rm -f "${default_link}"
    fi
}

    #
    # The RPM update command installs a given version of a package, and then
    # uninstalls all other versions of a package.
    #
    # The command does the following:
    #
    #     1) Run the %pre for the package being installed
    #     2) Install the new package's files
    #     3) Run the %post for the package being installed
    #     4) Run the %preun for each package being uninstalled
    #     5) Delete any old files not overwitten by the package being installed
    #     6) Run the %postun for each package being uninstalled
    #
    # Note: Because each version of Java installs into its own unique directory,
    #       the only files in step 5 that might not be deleted are the files in
    #       /etc/.java/.systemPrefs that are used for the Preferences API.
    #
    # Note: The order described above is also the same order that occurs when a
    #       user installs a new version, then uninstalls an old version at a
    #       later date.  The only difference is the ammount of time that passes
    #       between steps 3 and 4.
    #
    # Because of this order, all changes made to the system by the package
    # being installed are made *before* any changes made by packages being
    # uninstalled. This means that it is important that the %preun and %postun
    # scriptlets are written in a way that does not break any integration just
    # setup by the new package.  This makes it very difficult to determine what
    # should and shouldn't be removed during %preun and %postun scriptlets.
    #
    # Packages written in the past have no idea what the future will hold.  This
    # is obvious, but it doesn't make it easy.  One option is to assume users
    # will always install newer versions over older versions, and will never
    # keep multiple versions of the same package installed at the same time.
    # This is actually the assumption that RPM is designed upon.
    #
    # However, the --force option can be used to force RPM to install an older
    # package; a so called downgrade.  In the past, Java RPM packages have
    # always attempted to provide special support for downgrades.  This can
    # cause a lot of trouble given the design of RPM.
    #
    # This spec follows the recomended RPM practice.  If the version being
    # uninstalled is not the latest version, then nothing is done.  However, if
    # the version being uninstalled is the latest, then anything setup by the
    # %post scriptlet that is not also tracked by the RPM database is removed.
    #
    # Unfortunately there are two damned kinds of Java installations for every
    # given release, i.e. a JDK and a JRE.  Because of this, it is possible that
    # this version being uninstalled is the latest version, and that the version
    # being left behind is the *same* version as this!
    #
    # In this case, it is necessary to fix anything just broken by the %preun
    # scriptlet.  This will only happen when the JDK is uninstalled, and the
    # JRE of the same version is still on the system.  For this, all that needs
    # to be done is to repair the default and latest links.

    #
    # Determine if a new latest link should be created.  This is done if
    # there is still an installed version of Java that is 1.6 up to the
    # the version of this package.
    #
    LATEST_JAVA_PATH="`find_latest_release`"
    if [ -n "${LATEST_JAVA_PATH}" ] &&
       [ `compare_java_by_version ${LATEST_JAVA_PATH} \
                                  version-1.6.0_45` -lt 0 ]
    then
        #
        # Only maintain the latest link if the latest version left on
        # the system is the ugly stepsister to this one, i.e. this is
	# the JDK, and the JRE of the same version remains.
        #
        # Note: if the latest is higher than the version of this
        #       package, then latest will either A) already exist,
        #       so there is nothing that needs to be done, or B) the
        #       latest link is no longer supported buy those versions,
        #       so this package shouldn't set it up.
        #
        setup_latest_link "${LATEST_JAVA_PATH}" "/usr/java/latest"
    fi

    if [ -z "${LATEST_JAVA_PATH}" ] ||
       [ `compare_java_by_version ${LATEST_JAVA_PATH} \
                                  version-1.6.0_45` -lt 0 ]
    then
        #
        # Only maintain the latest link if the latest version left on
        # the system is the ugly stepsister to this one, i.e. this is
	# the JDK, and the JRE of the same version remains.
        #
        # Note: again, the best policy is to assume that higher
        #       releases can take better care of themselves
        #

        #
        # Remove all system integration.
        #
        RemoveMailcap /etc/mailcap application/x-java-jnlp-file
        RemoveMimeTypes /etc/mime.types application/x-java-jnlp-file
	DisintegrateWithGnome
    fi

    if [ -n "${LATEST_JAVA_PATH}" ]; then
        #
        # We just removed the Prefernce API files, so restore them since there
        # is still a version of Java installed.
        #
        mkdir -p /etc/.java/.systemPrefs
        if [ -f /etc/.java/.systemPrefs/.system.lock.rpmsave ]; then
            mv /etc/.java/.systemPrefs/.system.lock.rpmsave \
               /etc/.java/.systemPrefs/.system.lock
        elif [ ! -f /etc/.java/.systemPrefs/.system.lock ]; then
            touch /etc/.java/.systemPrefs/.system.lock
        fi
        if [ -f /etc/.java/.systemPrefs/.systemRootModFile.rpmsave ]; then
            mv /etc/.java/.systemPrefs/.systemRootModFile.rpmsave \
               /etc/.java/.systemPrefs/.systemRootModFile
        elif [ ! -f /etc/.java/.systemPrefs/.systemRootModFile ]; then
            touch /etc/.java/.systemPrefs/.systemRootModFile
        fi
    fi

    if [ -e "/usr/java/latest" ]; then
        #
        # If the latest link exists, then make sure the default link exists.
        #
        # Note: instead of trying to determine whether or not the current latest
        #       installation is a JDK or a JRE, just assume it's a JDK.
        #
        setup_default_links "/usr/java/latest" "/usr/java/default" \
                            "/usr/bin" "java javaws jcontrol javac jar javadoc"

        #
        # If there is still an init script kicking around then restart/reinstall
        # it in case it was stopped/uninstalled during %preun.
        #
        if [ -x /etc/init.d/jexec ]; then
            #
            # Try to register the init script to the various run levels.  If
            # possible this is accomplished using an LSB defined install tool.
            # If that isn't available, then try to use chkconfig, which is
            # supported by Red Hat and Debian.  Otherwise it is up to the user
            # to get the script setup for their distribution.
            #
            if [ -x /usr/lib/lsb/install_initd ]; then
                /usr/lib/lsb/install_initd jexec > /dev/null 2>&1

                # start the service for the current session
                /etc/init.d/jexec start > /dev/null 2>&1
            elif [ -x /sbin/chkconfig ]; then
                /sbin/chkconfig --add jexec > /dev/null 2>&1

                # start the service for the current session
                /etc/init.d/jexec start > /dev/null 2>&1
            fi
        fi
    fi






%verifyscript -p /bin/sh
#
    # Make sure any new files are created with a secure access mask.  Do not use
    # chmod, since that would also change the rights of any existing files, and
    # we are only interested in setting the rights for new files.
    #
    umask 022

    #
    # The package assumes that Gnome is either installed, or going to be
    # installed, so if nothing currently exists, then install in the default
    # location.
    #
    # NOTE: These variables must be defined before all the shell function macros
    #       are included.
    #
    if [ -z "${GNOMEDIR}" ]; then
        GNOMEDIR=/usr
    fi

    #
    # RPM_INSTALL_PREFIX doesn't seem to be set by "alien" so the following
    # minor kludge allows some functionality on debian-like systems (such
    # a Ubuntu) which don't support packages.
    #
    if [ -z "${RPM_INSTALL_PREFIX}" ]; then
	RPM_INSTALL_PREFIX="/usr/java"
    fi

    #
    # Gross kludge for old SuSE distros: Even though they set the environment
    # variable GNOMEDIR to /opt/gnome, Gnome may really be in /opt/gnome2.
    # Go figure,... (I feel so unclean....)
    #
    if [ "${GNOMEDIR}" = "/opt/gnome" ] && [ -d "/opt/gnome2" ]; then
	GNOMEDIR="/opt/gnome2"
    fi

    INSTALL_JRE_PATH=${RPM_INSTALL_PREFIX}/jdk1.6.0_45
    if [ -e ${INSTALL_JRE_PATH}/jre/bin/java ]; then
	INSTALL_JRE_PATH=${INSTALL_JRE_PATH}/jre
    fi
    #
    # Add the shell function and related variables used by the verify script.
    #
    NS_COMMENT1="#--Netscape Communications Corporation MIME Information"
NS_COMMENT2="#Do not delete the above line. It is used to identify the file type."
NS_COMMENT3="#mime types added by Netscape Helper"
UpdateMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    command="$3"
    if [ -z "`grep -E \"^${mime_type}; ${command}$\" \"${mailcap_file}\" 2> /dev/null`" ]; then
        mc_comment="# Java Web Start"
        mc_text=
        if [ -w "${mailcap_file}" ]; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
        fi
        if [ -w "`dirname \"${mailcap_file}\"`" ]; then
            mc_text="${mc_text:+${mc_text}\n}${mime_type}; ${command}"
            printf "%s" "${mc_text}" > "${mailcap_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mailcap_file}"
            echo "Check permissions."
        fi
    fi
}
RemoveMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    mc_comment="# Java Web Start"
    if [ -w "${mailcap_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mailcap_file}\"`" ] ; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
            if [ `echo "${mc_text}" | tr -d '[:space:]' | wc -c` -gt 0 ]; then
                echo "${mc_text}" > "${mailcap_file}"
            else
                rm -f "${mailcap_file}"
            fi
        fi
    fi
}
UpdateMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    desc="$3"
    shift 3
    exts="$*"
    JNLP_ENTRY="type=${mime_type} desc=\"${desc}\" exts=\"${exts}\""
    if [ ! -w "${mime_file}" ]; then
        if [ -w `dirname ${mime_file}` ]; then
            echo "${NS_COMMENT1}"  > "${mime_file}"
            echo "${NS_COMMENT2}" >> "${mime_file}"
            echo "${NS_COMMENT3}" >> "${mime_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mime_file}"
            echo "Check permissions."
            return
        fi
    fi
    if [ -z "`grep -E \"^[^#]*${mime_type}\" \"${mime_file}\"`" ]; then
        echo ${JNLP_ENTRY} >> "${mime_file}"
    fi
}
RemoveMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    if [ -w "${mime_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mime_file}\"`" ]; then
            regexp="(${mime_type})|(^${NS_COMMENT1}$)|(^${NS_COMMENT2}$)|(^${NS_COMMENT3}$)"
            if [ `grep -Ev "${regexp}" "${mime_file}" | \
                 tr -d '[:space:]' | wc -c` -gt 0 ]
            then
                mt_text="`grep -v \"${mime_type}\" \"${mime_file}\"`"
                echo "${mt_text}" > "${mime_file}"
            else
                rm -f "${mime_file}"
            fi
        fi
    fi
}
    JDK_DESKTOP="${INSTALL_JRE_PATH}/lib/desktop"
JDK_ICONS="${JDK_DESKTOP}/icons"
JDK_APPS="${JDK_DESKTOP}/applications"
JDK_MIME="${JDK_DESKTOP}/mime"
SHARE_PATH="${GNOMEDIR}/share"
SHARE_ICONS="${SHARE_PATH}/icons"
SHARE_MIME="${SHARE_PATH}/mime"
SHARE_APPS="${SHARE_PATH}/applications"
HICOLOR=hicolor
HIGHCONTRAST=HighContrast
HIGHCONTRASTINVERSE=HighContrastInverse
LOWCONTRAST=LowContrast
THEMES="${HICOLOR} ${HIGHCONTRAST} ${HIGHCONTRASTINVERSE} ${LOWCONTRAST}"
RESOLUTIONS="16x16 48x48"
TEXT_ICON="gnome-mime-text-x-java.png"
JAR_ICON="gnome-mime-application-x-java-archive.png"
JNLP_ICON="gnome-mime-application-x-java-jnlp-file.png"
JAVA_ICON="sun-java.png"
JAVAWS_ICON="sun-javaws.png"
JCONTROL_ICON="sun-jcontrol.png"
APPS_ICONS="${JAVA_ICON} ${JAVAWS_ICON} ${JCONTROL_ICON}"
MIME_ICONS="${TEXT_ICON} ${JAR_ICON} ${JNLP_ICON}"
ICONS="${APPS_ICONS} ${MIME_ICONS}"
GNOME_UTILS_DIRS="/usr/bin /opt/gnome/bin"
UPDATE_MIME_DATABASE="update-mime-database"
UPDATE_DESKTOP_DATABASE="update-desktop-database"
GTK_UPDATE_ICON_CACHE="gtk-update-icon-cache"
SHARE_CONTROL_CENTER="${SHARE_PATH}/control-center-2.0"
SHARE_CAPPLETS="${SHARE_CONTROL_CENTER}/capplets"
SHARE_MIME_INFO="${SHARE_PATH}/mime-info"
SHARE_APP_REGISTRY="${SHARE_PATH}/application-registry"
SHARE_PIXMAPS="${SHARE_PATH}/pixmaps"
UpdateIconCache() {
    _icon_theme_root=$1
    if [ -f ${_icon_theme_root}/icon-theme.cache ]; then
	for _dir in ${GNOME_UTILS_DIRS}; do
	    if [ -x ${_dir}/${GTK_UPDATE_ICON_CACHE} ]; then
		${_dir}/${GTK_UPDATE_ICON_CACHE} ${_icon_theme_root} \
		    > /dev/null 2>&1
		break
	    fi
	done
	touch ${_icon_theme_root}
	for _dir in ${RESOLUTIONS}; do
	    if [ -d ${_icon_theme_root}/${_dir} ]; then
		touch ${_icon_theme_root}/${_dir}
	    fi
        done
    fi
}
UpdateDesktopDatabase() {
    _desktop_root=$1
    if [ -f ${_desktop_root}/mimeinfo.cache ]; then
	for _dir in ${GNOME_UTILS_DIRS}; do
	    if [ -x ${_dir}/${UPDATE_DESKTOP_DATABASE} ]; then
		${_dir}/${UPDATE_DESKTOP_DATABASE} ${_desktop_root} \
		   > /dev/null 2>&1
		break
	    fi
	done
    fi
}
UpdateMimeDatabase() {
    _mime_root=$1
    if [ -d ${_mime_root}/packages ]; then
	for _dir in ${GNOME_UTILS_DIRS}; do
	    if [ -x ${_dir}/${UPDATE_MIME_DATABASE} ]; then
		${_dir}/${UPDATE_MIME_DATABASE} ${_mime_root} > /dev/null 2>&1
		break
	    fi
	done
    fi
}
InstallGnomeIcons() {
    for _theme in ${THEMES}; do
	if [ -d ${SHARE_ICONS}/${_theme} ]; then
	    for _res in ${RESOLUTIONS}; do
		mkdir -p ${SHARE_ICONS}/${_theme}/${_res}/apps
		for _icon in ${APPS_ICONS}; do
		    cp -f ${JDK_ICONS}/${_theme}/${_res}/apps/${_icon} \
			  ${SHARE_ICONS}/${_theme}/${_res}/apps/${_icon}
		done
		mkdir -p ${SHARE_ICONS}/${_theme}/${_res}/mimetypes
		for _icon in ${MIME_ICONS}; do
		    cp -f ${JDK_ICONS}/${_theme}/${_res}/mimetypes/${_icon} \
			  ${SHARE_ICONS}/${_theme}/${_res}/mimetypes/${_icon}
		done
	    done
	    UpdateIconCache ${SHARE_ICONS}/${_theme}
	fi
    done
    if [ -d ${SHARE_PIXMAPS} ]; then
	for _icon in ${APPS_ICONS}; do
	    cp -f ${JDK_ICONS}/${HICOLOR}/48x48/apps/${_icon} \
		  ${SHARE_PIXMAPS}/${_icon}
	done
	cp -f ${JDK_ICONS}/${HICOLOR}/48x48/mimetypes/${TEXT_ICON} \
	      ${SHARE_PIXMAPS}/x-java.png
	cp -f ${JDK_ICONS}/${HICOLOR}/48x48/mimetypes/${JAR_ICON} \
	      ${SHARE_PIXMAPS}/x-java-archive.png
	cp -f ${JDK_ICONS}/${HICOLOR}/48x48/mimetypes/${JNLP_ICON} \
	      ${SHARE_PIXMAPS}/x-java-jnlp-file.png
    fi
}
RemoveGnomeIcons() {
    for _theme in ${THEMES}; do
	for _res in ${RESOLUTIONS}; do
	    for _icon in ${APPS_ICONS}; do
		rm -f ${SHARE_ICONS}/${_theme}/${_res}/apps/${_icon}
	    done
	    for _icon in ${MIME_ICONS}; do
		rm -f ${SHARE_ICONS}/${_theme}/${_res}/mimetypes/${_icon}
	    done
	done
	UpdateIconCache ${SHARE_ICONS}/${_theme}
    done
    if [ -d ${SHARE_PIXMAPS} ]; then
	for _icon in ${APPS_ICONS}; do
	    rm -f ${SHARE_PIXMAPS}/${_icon}
	done
	rm -f ${SHARE_PIXMAPS}/x-java.png
	rm -f ${SHARE_PIXMAPS}/x-java-archive.png
	rm -f ${SHARE_PIXMAPS}/x-java-jnlp-file.png
    fi
}
InstallGnomeDesktop() {
    _file=$1
    mkdir -p ${SHARE_APPS}
    cp -f ${JDK_APPS}/${_file} ${SHARE_APPS}/${_file}
    if [ "${_file}" = "sun_java.desktop" ]; then
	if [ -d ${SHARE_CAPPLETS} ]; then
	    cp -f ${JDK_APPS}/${_file} ${SHARE_CAPPLETS}/${_file}
	fi
    fi
}
RemoveGnomeDesktop() {
    _file=$1
    rm -f ${SHARE_APPS}/${_file}
    rm -f ${SHARE_CAPPLETS}/${_file}
}
InstallLegacyMimetype() {
    _mime_type=$1
    _extension=$2
    _name=$3
    _command=$4
    _icon=$5
    _description=$6
    cat <<- end_of_keys_file > ${SHARE_MIME_INFO}/${_name}.keys
	${_mime_type}:
	    description=${_description}
	    icon_filename=${_icon}
	    default_action_type=application
	    default_application_id=${_name}
	    short_list_application_user_additions=${_name}
	end_of_keys_file
    cat <<- end_of_mime_file > ${SHARE_MIME_INFO}/${_name}.mime
	${_mime_type}
	    ext: ${_extension}
	end_of_mime_file
    cat <<- end_of_apps_file > ${SHARE_APP_REGISTRY}/${_name}.applications
	${_name}
	    command=${_command}
	    name=${_name}
	    can_open_multiple_files=false
	    requires_terminal=false
	    mime_types=${_mime_type}
	end_of_apps_file
}
RemoveLegacyMimetype() {
    _name=$1
    rm -f ${SHARE_MIME_INFO}/${_name}.keys
    rm -f ${SHARE_MIME_INFO}/${_name}.mime
    rm -f ${SHARE_APP_REGISTRY}/${_name}.applications
}
InstallGnomeMimetypes() {
    if [ -d ${SHARE_MIME} ]; then
	cp -f ${JDK_MIME}/packages/x-java-archive.xml \
	      ${SHARE_MIME}/packages/x-java-archive.xml
	cp -f ${JDK_MIME}/packages/x-java-jnlp-file.xml \
	      ${SHARE_MIME}/packages/x-java-jnlp-file.xml
    fi
    UpdateMimeDatabase ${SHARE_MIME}
    if [ -d ${SHARE_MIME_INFO} ] || [ -d ${SHARE_APP_REGISTRY} ]; then
	mkdir -p ${SHARE_MIME_INFO}
	mkdir -p ${SHARE_APP_REGISTRY}
	InstallLegacyMimetype application/x-java-archive \
                 jar              \
                 java-archive     \
                 "java -jar"      \
                 x-java-archive.png     \
		 "Java Archive"
	InstallLegacyMimetype application/x-java-jnlp-file \
                 jnlp                \
                 java-web-start      \
                 javaws              \
                 x-java-jnlp-file.png        \
                 "Java Web Start Application"
    fi
}
RemoveGnomeMimetypes() {
    rm -f ${SHARE_MIME}/packages/x-java-archive.xml
    rm -f ${SHARE_MIME}/packages/x-java-jnlp-file.xml
    UpdateMimeDatabase ${SHARE_MIME}
    if [ -d ${SHARE_MIME_INFO} ] || [ -d ${SHARE_APP_REGISTRY} ]; then
	RemoveLegacyMimetype java-archive
	RemoveLegacyMimetype java-web-start
    fi
}
IntegrateWithGnome() {
    InstallGnomeIcons
    InstallGnomeDesktop sun_java.desktop
    InstallGnomeDesktop sun-java.desktop
    InstallGnomeDesktop sun-javaws.desktop
    UpdateDesktopDatabase ${SHARE_APPS}
    InstallGnomeMimetypes
}
DisintegrateWithGnome() {
    RemoveGnomeIcons
    RemoveGnomeDesktop sun_java.desktop
    RemoveGnomeDesktop sun-java.desktop
    RemoveGnomeDesktop sun-javaws.desktop
    UpdateDesktopDatabase ${SHARE_APPS}
    RemoveGnomeMimetypes
}
    MOST_DIGITS="[1-9]"
ALL_DIGITS="[0-9]"
COUNTING_NUMBER="${MOST_DIGITS}${ALL_DIGITS}*\|0"
VALID_NON_NUMERIC="[-_.a-zA-Z]"
VALID_CHARS="[-_.a-zA-Z0-9]"
MAJOR_RULE="\(${MOST_DIGITS}${ALL_DIGITS}*\)"
MINOR_RULE="\(${COUNTING_NUMBER}\)"
MICRO_RULE="\(${COUNTING_NUMBER}\)"
UPDATE_RULE="\(${MOST_DIGITS}${ALL_DIGITS}\|0${ALL_DIGITS}\)"
NON_FCS_ID_RULE="\([a-zA-Z0-9]*\)"
MIN_VERSION_ID_RULE="${MAJOR_RULE}\.${MINOR_RULE}\.${MICRO_RULE}"
FCS_VERSION_ID_RULE="${MIN_VERSION_ID_RULE}\(_${UPDATE_RULE}\)\?"
VERSION_ID_RULE="${FCS_VERSION_ID_RULE}\(-${NON_FCS_ID_RULE}\)\?"
NAME_ID_RULE="${VALID_CHARS}*${VALID_NON_NUMERIC}"
KNOWN_GOOD_NAME_LIST="java jdk jre j2sdk j2re"
PRS_ERROR_BAD_PARAMS=2000
expand_version() {
    status=0
    if [ $# -eq 0 ]; then
        read release remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${release}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${release}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        release=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        \printf "\t expand_version\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        format="%d\t%d\t%d\t%d\n"
        echo ${release} | sed -e "s/_/\./g" | \
          awk -v format="${format}" 'BEGIN { FS = "." } { printf format, $1, $2, $3, $4 }'
    fi
    return ${status}
}
parse_release() {
    status=0
    if [ $# -eq 0 ]; then
        read string remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${string}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${string}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        string=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t parse_release %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        version_id=`expr "${string}" : "${NAME_ID_RULE}\(${VERSION_ID_RULE}\)\$"`
        if [ -n "${version_id}" ]; then
            name_id=`expr "${string}" : "\(${NAME_ID_RULE}\)${VERSION_ID_RULE}\$"`
            fcs_part=`expr "${string}" : "${NAME_ID_RULE}\(${FCS_VERSION_ID_RULE}\).*\$"`
            non_fcs_part=`expr "${version_id}" : "[^-]*-\(${NON_FCS_ID_RULE}\)\$"`
	    printf "%s\t%s\t%s\n" "${name_id}" "${fcs_part}" "${non_fcs_part}"
        fi
    fi
    return ${status}
}
UNKNOWN_NAME_WEIGHT=1000
get_name_weight() {
    status=0
    if [ "$1" = "-" ]; then
        read name good_names
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        else
            shift 1
            if [ $# -gt 0 ]; then
                good_names="$*"
            fi
            if [ -z "${name}" ]; then
                printf "Error: usage - function requires input!\n" >> /dev/stderr
                status=${PRS_ERROR_BAD_PARAMS}
            fi
        fi
    elif [ $# -gt 1 ]; then
        name=$1
        shift 1
        good_names="$*"
    else
        printf "Error: usage - function takes 2+ parameters:\n\n" >> /dev/stderr
        printf "\t get_name_weight %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -n "${good_names}" ]; then
            length=`expr length "${good_names}"`
            pos=`expr "${good_names}" : ".*\<${name}\>"`
            if [ ${pos} -gt 0 ]; then
                expr substr "${good_names}" 1 ${pos} | wc -w | tr -d "[:space:]"
            else
                echo ${UNKNOWN_NAME_WEIGHT}
            fi
        else
            echo ${UNKNOWN_NAME_WEIGHT}
        fi
    fi
    return ${status}
}
HAS_FCS_WEIGHT=0
HAS_ODD_FCS_WEIGHT=1
HAS_RC_WEIGHT=100
HAS_ODD_RC_WEIGHT=101
HAS_BETA_WEIGHT=300
HAS_ODD_BETA_WEIGHT=301
HAS_EA_WEIGHT=500
HAS_ODD_EA_WEIGHT=501
HAS_INTRNAL_WEIGHT=2000
HAS_VERY_ODD_WEIGHT=9999
get_non_fcs_weight() {
    status=0
    if [ $# -eq 0 ]; then
        read non_fcs_part remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${non_fcs_part}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        non_fcs_part=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t get_non_fcs_weight \n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -z "${non_fcs_part}" ]; then
            echo ${HAS_FCS_WEIGHT}
        else
            case "${non_fcs_part}" in
                fcs)
                    echo ${HAS_ODD_FCS_WEIGHT}
                    ;;
                rc)
                    echo ${HAS_RC_WEIGHT}
                    ;;
                rc[0-9] | rc[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "rc\([0-9]*\)$"`
                    echo `expr ${HAS_RC_WEIGHT} - ${count}`
                    ;;
                rc*)
                    echo ${HAS_ODD_RC_WEIGHT}
                    ;;
                beta)
                    echo ${HAS_BETA_WEIGHT}
                    ;;
                beta[0-9] | beta[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "beta\([0-9]*\)$"`
                    echo `expr ${HAS_BETA_WEIGHT} - ${count}`
                    ;;
                beta*)
                    echo ${HAS_ODD_BETA_WEIGHT}
                    ;;
                ea)
                    echo ${HAS_EA_WEIGHT}
                    ;;
                ea[0-9] | ea[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "ea\([0-9]*\)$"`
                    echo `expr ${HAS_EA_WEIGHT} - ${count}`
                    ;;
                ea*)
                    echo ${HAS_ODD_EA_WEIGHT}
                    ;;
                internal)
                    echo ${HAS_INTRNAL_WEIGHT}
                    ;;
                internal[0-9] | internal[0-9][0-9] | internal[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "internal\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                b[0-9] | b[0-9][0-9] | b[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "b\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                *)
                    echo ${HAS_VERY_ODD_WEIGHT}
                    ;;
            esac
        fi
    fi
    return ${status}
}
    get_path_weight() {
    good_list="$1"
    path=$2
    release=`basename ${path}`
    parts="`parse_release ${release}`"
    if [ $? -eq 0 ]; then
        name=`echo "${parts}" | cut -f1`
        version=`echo "${parts}" | cut -f2`
        non_fcs=`echo "${parts}" | cut -f3`
        if [ -n "${version}" ]; then
           v_weight=`echo ${version} | expand_version`
           n_weight=`echo ${name} | get_name_weight - "${good_list}"`
           o_weight=`echo ${non_fcs} | get_non_fcs_weight`
           printf "%4d  %4d  %4d  %4d  %4d  %4d  %s\n" \
                  ${v_weight} ${n_weight} ${o_weight} "${path}"
        fi
    fi
}
get_weighted_list() {
    good_list=
    verify=
    stdio=
    status=0
    check=true
    while [ -n "${check}" ]; do
        if [ $# -gt 0 ]; then
            case "$1" in
                -g)
                    good_list="$2"
                    shift 2
                    ;;
                --good-list=*)
                    length=`expr length "$1"`
                    remove=`expr \( length "--good-list=" \) + 1`
                    good_list="`expr substr \"$1\" ${remove} ${length}`"
                    shift 1
                    ;;
                -v | --verify)
                    verify=true
                    shift 1
                    ;;
                --)
                    shift 1
                    check=
                    ;;
                -)
                    shift 1
                    stdio=true
                    ;;
                -*)
                    printf "Error: usage - unknown parameter:\n\n" \
								>> /dev/stderr
                    printf "\t%s : %s\n" "$1" "$*"		>> /dev/stderr
                    status=${PRS_ERROR_BAD_PARAMS}
                    check=
                    ;;
                *)
                    check=
                    ;;
            esac
        else
            check=
        fi
    done
    if [ $# -eq 0 ] || [ -n "${stdio}" ]; then
        read line
        while [ -n "${line}" ]; do
            if [ -z "${verify}" ] || [ -f ${line}/bin/java ]; then
                get_path_weight "${good_list}" ${line}
            fi
            read line
        done
    fi
    while [ $# -gt 0 ]; do
        if [ -z "${verify}" ] || [ -f $1/bin/java ]; then
            get_path_weight "${good_list}" $1
        fi
        shift 1
    done
    return ${status}
}
_compare_java_by_weight() {
    compare=0
    if [ $# -ne 0 ]; then
        if [ $# -eq 1 ]; then
            compare=1
        else
            left=$1
            right=$2
            shift 2
            good="$*"
            list=`get_weighted_list --good-list="${good}" \
                    ${left} ${right} | sort -u -k1n -k2n -k3n -k4n -k5rn -k6rn`
            if [ `echo "${list}" | wc -l | tr -d "[:space:]"` -ne 1 ]; then
                compare=-1
                latest=`echo "${list}" | tail -n 1 | cut -c 37-`
                if [ "${left}" = "${latest}" ]; then
                    compare=1
                fi
            fi
        fi
    fi
    echo ${compare}
}
compare_java_by_version() {
    _compare_java_by_weight $1 $2
}
compare_java_by_release() {
    _compare_java_by_weight $1 $2 ${KNOWN_GOOD_NAME_LIST}
}
find_latest_release() {
    if [ -d /usr/java ]; then
        latest_release=`find /usr/java/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
    fi
    if [ -d "${RPM_INSTALL_PREFIX}" ] && \
       [ "/usr/java" != "${RPM_INSTALL_PREFIX}" ]
    then 
        prefix_release=`find ${RPM_INSTALL_PREFIX}/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
        if [ `compare_java_by_release ${latest_release} ${prefix_release}` -lt 0 ]; then
            latest_release=${prefix_release}
        fi
    fi
    echo ${latest_release}
}
get_javaws() {
    path=$1
    if [ `compare_java_by_version ${path} version-1.5.0` -ge 0 ] &&
       [ -f ${path}/bin/javaws ]
    then
        path=${path}/bin/javaws
    elif [ `compare_java_by_version ${path} version-1.4.2` -ge 0 ]; then
        if [ -f ${path}/jre/javaws/javaws ]; then
            path=${path}/jre/javaws/javaws
        elif [ -f ${path}/javaws/javaws ]; then
            path=${path}/javaws/javaws
        else
            path=
        fi
    else
        path=
    fi
    echo ${path}
}
    LINK_ERROR_BAD_PARAMS=3000
LINK_ERROR_DEAD_LINK=3001
LINK_ERROR_FILE_NOT_FOUND=3002
dereference() {
    status=0
    if [ "$1" = "-f" ] || [ "$1" = "--follow" ]; then
        follow="--follow"
        shift 1
    fi
    if [ $# -ge 1 ]; then
        path="$*"
        if [ -e "${path}" ]; then
            parent="`cd \`dirname \"${path}\"\`; pwd`"
            child="`basename \"${path}\"`"
            if [ "${parent}" != "${child}" ]; then
                path="${parent}/${child}"
            fi
            if [ -h "${path}" ]; then
                path=`ls -l "${path}" | sed -e "s#^.*${path} -> ##"`
                if [ "`expr substr \"${path}\" 1 1`" != "/" ]; then
                    path="${parent}/${path}"
                fi
                if [ -n "${follow}" ]; then
                    path="`dereference ${follow} ${path}`"
                fi                    
            fi
        else
            status=${LINK_ERROR_FILE_NOT_FOUND}
        fi
    fi
    echo ${path}
    return ${status}
}
setup_latest_link() {
    latest=$1
    link=$2
    if [ -h "${link}" ]; then
        reference="`dereference --follow ${link}`"
        if [ $? -eq 0 ]; then
            update=`compare_java_by_release "${latest}" "${reference}"`
        else
            update=1
        fi
        if [ ${update} -gt 0 ]; then
            rm -f "${link}"
        fi
    fi
    if [ ! -e "${link}" ]; then
        ln -s "${latest}" "${link}"
    fi
}
setup_default_links() {
    if [ $# -ge 2 ]; then
        latest_link="$1"
        default_link="$2"
        if [ ! -e "${default_link}" ]; then
            ln -s "${latest_link}" "${default_link}"
        fi
    fi
    if [ $# -gt 3 ]; then
        bindir="$3"
        shift 3
        for file in $*; do
            reference="`dereference --follow ${bindir}/${file}`"
            if [ $? -ne 0 ]; then
                rm -f "${bindir}/${file}"
            fi
            source="${default_link}/bin/${file}"
            if [ "${file}" = "javaws" ]; then
                source="`get_javaws \"${default_link}\"`"
            fi
            if [ -n "${source}" ] && [ ! -e "${bindir}/${file}" ]; then
                ln -s "${source}" "${bindir}/${file}"
            fi
        done
    fi
}
cleanup_default_links() {
    if [ $# -ge 1 ]; then
        default_link=$1
        if [ $# -gt 2 ]; then
            bindir="$2"
            shift 2
            for file in $*; do
                reference="`dereference \"${bindir}/${file}\"`"
                if [ $? -ne 0 ] ||
                   [ "${reference}" = "${default_link}/bin/${file}" ]
                then
                    rm -f "${bindir}/${file}"
                fi
            done
        fi
        rm -f "${default_link}"
    fi
}

    #
    # It isn't possible to repair any missing packed JAR files from --verify.
    # This is because the PACK source files are removed during post-install.
    # If an administrator needs to restore missing packed JAR files, they will
    # need to do a --reinstall.
    #

    #
    # If the package was relocated, then temporarily remove the /usr/java
    # link, but only if it really points to this package.
    #
    if [ "${RPM_INSTALL_PREFIX}" != "/usr/java" ] &&
       [ "`dereference --follow \"/usr/java/jdk1.6.0_45\"`" = "${RPM_INSTALL_PREFIX}" ]
    then
        rm -f "/usr/java/jdk1.6.0_45"
    fi

    #
    # Find out what version of Java is the latest.  Don't do any system
    # integration unless this is the latest version.  Otherwise, we make
    # it difficult for future installers.
    #
    LATEST_JAVA_PATH="`find_latest_release`"
    if [ "${LATEST_JAVA_PATH}" == "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ] ||
       [ "${LATEST_JAVA_PATH}" == "/usr/java/jdk1.6.0_45" ]
    then
        #
        # Make sure the /usr/java/latest link points to LATEST_JAVA_PATH, and
	# update it if it doesn't.
        #
        setup_latest_link "${LATEST_JAVA_PATH}" "/usr/java/latest"

        #
        # Make sure the /usr/java/default and java javaws jcontrol javac jar javadoc exist.
	# If anything is missing, create it.
        #
        setup_default_links "/usr/java/latest" "/usr/java/default" \
                            "/usr/bin" java javaws jcontrol javac jar javadoc

        #
        # If the "latest" link is a JDK, then the latest JRE is a subdir;
	# otherwise it is the same dir.
        #
        DEFAULT_JRE_PATH="/usr/java/default"
        if [ -e "/usr/java/default/jre/bin/java" ]; then
            DEFAULT_JRE_PATH="/usr/java/default/jre"
        fi

	#
	IntegrateWithGNOME

        # setup the mailcap file
        UpdateMailcap /etc/mailcap application/x-java-jnlp-file "/usr/bin/javaws %s"

        # setup the mime.type file
        UpdateMimeTypes /etc/mime.types	application/x-java-jnlp-file \
			"Java Web Start" jnlp
    fi

    #
    # If the package is being relocated, then create a link in the default
    # location (/usr/java) to the actual install directory.  Do this
    # last, so it doesn't add unnecessary complexity to the search for the
    # latest release.
    #
    if [ "${RPM_INSTALL_PREFIX}" != "/usr/java" ] &&
       ( [ ! -e "/usr/java/jdk1.6.0_45" ] || [ -h "/usr/java/jdk1.6.0_45" ] )
    then
        rm -f "/usr/java/jdk1.6.0_45"
        ln -s "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" "/usr/java/jdk1.6.0_45"
    fi

    #
    # There should be an init script for jexec on the system.  If it is, then
    # make sure it's installed and running
    #
    if [ -x /etc/init.d/jexec ]; then
        #
        # Try to register the init script to the various run levels.  If
	# possible this is accomplished using an LSB defined install tool.
	# If that isn't available, then try to use chkconfig, which is
	# supported by Red Hat and Debian.  The feature of automatic jar
	# file execution is not support on systems which don't support
	# either of these interfaces.
        #
        if [ -x /usr/lib/lsb/install_initd ]; then
            /usr/lib/lsb/install_initd jexec > /dev/null 2>&1

            # start the service for the current session
            /etc/init.d/jexec start > /dev/null 2>&1
        elif [ -x /sbin/chkconfig ]; then
            /sbin/chkconfig --add jexec > /dev/null 2>&1

            # start the service for the current session
            /etc/init.d/jexec start > /dev/null 2>&1
        fi
    fi




%changelog
* Wed May 01 2013 root - 1.6.0_45-fcs.1
- Specfile created from binary rpm jdk-6u45-linux-i586.rpm
%endif

%ifarch x86_64
%global __os_install_post %{nil}
%global __spec_install_post %{nil}
%global __debug_install_post %{nil}
%global debug_package %{nil}
%undefine __debug_package
%undefine _enable_debug_packages
Name: jdk
Epoch: 2000
Version: 1.6.0_45
Release: fcs.1%{?dist}
Group: Development/Tools
URL: http://www.oracle.com/technetwork/java/javase/overview/index.html
License: Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved. Also under other license(s) as shown at the Description field.
Summary: Java(TM) Platform Standard Edition Development Kit
Source0: jdk-6u45-linux-i586.bin.tar.gz
Source1: jdk-6u45-linux-amd64.bin.tar.gz
AutoReqProv: no
Prefix: /usr/java
Requires: /bin/basename
Requires: /bin/cat
Requires: /bin/cp
Requires: /bin/gawk
Requires: /bin/grep
Requires: /bin/ln
Requires: /bin/ls
Requires: /bin/mkdir
Requires: /bin/mv
Requires: /bin/pwd
Requires: /bin/rm
Requires: /bin/sed
Requires: /bin/sort
Requires: /bin/touch
Requires: /usr/bin/cut
Requires: /usr/bin/dirname
Requires: /usr/bin/expr
Requires: /usr/bin/find
Requires: /usr/bin/tail
Requires: /usr/bin/tr
Requires: /usr/bin/wc
Requires: /bin/sh
Provides: jaxp_parser_impl
Provides: xml-commons-apis
Provides: jdk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
The Java Platform Standard Edition Development Kit (JDK) includes both
the runtime environment (Java virtual machine, the Java platform classes
and supporting files) and development tools (compilers, debuggers,
tool libraries and other tools).

The JDK is a development environment for building applications, applets
and components that can be deployed with the Java Platform Standard
Edition Runtime Environment.



%prep
%setup -n jdk-6u45-linux-amd64.extract -T -b 1



%build
exit 0



%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mv * $RPM_BUILD_ROOT
pushd $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/plugin.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/plugin.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/ext/localedata.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/ext/localedata.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/javaws.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/javaws.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/jsse.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/jsse.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/lib/tools.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/lib/tools.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/deploy.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/deploy.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/charsets.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/charsets.jar
mkdir -p $RPM_BUILD_ROOT/$(dirname /usr/java/jdk1.6.0_45/jre/lib/rt.jar)
touch $RPM_BUILD_ROOT/usr/java/jdk1.6.0_45/jre/lib/rt.jar

popd


%files
%defattr(-,root,root,-)
%dir %verify(group md5 size link mtime user mode rdev) /etc/.java
%dir %verify(group md5 size link mtime user mode rdev) /etc/.java/.systemPrefs
%config(noreplace) %verify(group link user mode rdev) /etc/.java/.systemPrefs/.system.lock
%config(noreplace) %verify(group link user mode rdev) /etc/.java/.systemPrefs/.systemRootModFile
%attr(0755,root,root) %config() %verify(group link user mode rdev) /etc/init.d/jexec
%dir %verify(group md5 size link mtime user mode rdev) /usr/java
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/COPYRIGHT
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/LICENSE
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/README.html
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/THIRDPARTYLICENSEREADME.txt
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/ControlPanel
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/HtmlConverter
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/appletviewer
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/apt
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/extcheck
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/idlj
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jar
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jarsigner
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/java
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javac
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javadoc
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javah
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javap
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/javaws
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jconsole
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jcontrol
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jdb
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jhat
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jinfo
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jmap
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jps
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jrunscript
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jsadebugd
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jstack
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jstat
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jstatd
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/jvisualvm
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/keytool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/native2ascii
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/orbd
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/pack200
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/policytool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/rmic
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/rmid
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/rmiregistry
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/schemagen
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/serialver
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/servertool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/tnameserv
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/unpack200
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/wsgen
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/wsimport
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/bin/xjc
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/classfile_constants.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/jawt.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/jdwpTransport.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/jni.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/jvmti.h
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/linux
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/linux/jawt_md.h
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/include/linux/jni_md.h
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/COPYRIGHT
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/LICENSE
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/README
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/THIRDPARTYLICENSEREADME.txt
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/Welcome.html
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/ControlPanel
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/java
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/java_vm
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/javaws
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/jcontrol
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/keytool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/orbd
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/pack200
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/policytool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/rmid
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/rmiregistry
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/servertool
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/tnameserv
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/bin/unpack200
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/javaws
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/javaws/javaws
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/alt-rt.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/alt-string.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/headless
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/headless/libmawt.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/jli
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/jli/libjli.so
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/jvm.cfg
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libJdbcOdbc.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libattach.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libawt.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libcmm.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libdcpr.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libdeploy.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libdt_socket.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libfontmanager.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libhprof.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libinstrument.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libioser12.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libj2gss.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libj2pcsc.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libj2pkcs11.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjaas_unix.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjava.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjava_crw_demo.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjavaplugin_jni.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjawt.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjdwp.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjpeg.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjsig.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjsound.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libjsoundalsa.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libmanagement.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libmlib_image.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libnative_chmod.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libnative_chmod_g.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libnet.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libnio.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libnpjp2.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libnpt.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/librmi.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libsaproc.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libsplashscreen.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libunpack.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libverify.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/libzip.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/motif21
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/motif21/libmawt.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/native_threads
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/native_threads/libhpi.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/server
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/server/Xusage.txt
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/server/libjsig.so
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/server/libjvm.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/xawt
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/amd64/xawt/libmawt.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/applet
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/audio
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/audio/soundbank.gm
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/calendars.properties
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/charsets.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/charsets.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/classlist
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/CIEXYZ.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/GRAY.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/LINEAR_RGB.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/PYCC.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/cmm/sRGB.pf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/content-types.properties
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/ffjcext.zip
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/java-icon.ico
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_de.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_es.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_fr.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_it.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_ja.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_ko.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_pt_BR.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_sv.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_zh_CN.properties
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_zh_HK.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/messages_zh_TW.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/deploy/splash.gif
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/applications
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/applications/sun-java.desktop
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/applications/sun-javaws.desktop
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/applications/sun_java.desktop
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/16x16/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrast/48x48/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/16x16/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/HighContrastInverse/48x48/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/16x16/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/LowContrast/48x48/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/16x16/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/apps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/apps/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/apps/sun-javaws.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/apps/sun-jcontrol.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/mimetypes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-java-archive.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-java-jnlp-file.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/icons/hicolor/48x48/mimetypes/gnome-mime-text-x-java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/mime
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/mime/packages
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/mime/packages/x-java-archive.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/desktop/mime/packages/x-java-jnlp-file.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/dnsns.jar
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/localedata.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/localedata.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/meta-index
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/sunjce_provider.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/ext/sunpkcs11.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/flavormap.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.2.1.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.2.1.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.3.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.3.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.4.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.4.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.6.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.6.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.RedHat.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.SuSE.11.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.SuSE.11.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.SuSE.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.SuSE.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Sun.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Sun.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Turbo.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Turbo.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Ubuntu.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.Ubuntu.properties.src
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.bfc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fontconfig.properties.src
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaBrightDemiBold.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaBrightDemiItalic.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaBrightItalic.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaBrightRegular.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaSansDemiBold.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaSansRegular.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaTypewriterBold.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/LucidaTypewriterRegular.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/fonts/fonts.dir
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/im
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/im/indicim.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/im/thaiim.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/cursors.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/invalid32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_CopyDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_CopyNoDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_LinkDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_LinkNoDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_MoveDrop32x32.gif
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/cursors/motif_MoveNoDrop32x32.gif
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons/sun-java.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons/sun-java_HighContrast.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons/sun-java_HighContrastInverse.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/images/icons/sun-java_LowContrast.png
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/javaws.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/javaws.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jce.jar
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jexec
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jsse.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jsse.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/jvm.hprof.txt
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/de
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/de/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/de/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/es
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/es/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/es/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/fr
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/fr/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/fr/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/it
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/it/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/it/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ja
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ja/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ja/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko.UTF-8
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko.UTF-8/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko.UTF-8/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/ko/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/sv
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/sv/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/sv/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh.GBK
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh.GBK/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh.GBK/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_HK.BIG5HK
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_HK.BIG5HK/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_HK.BIG5HK/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW.BIG5
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW.BIG5/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW.BIG5/LC_MESSAGES/sunw_java_plugin.mo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW/LC_MESSAGES
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/locale/zh_TW/LC_MESSAGES/sunw_java_plugin.mo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/logging.properties
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management-agent.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management/jmxremote.access
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management/jmxremote.password.template
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management/management.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/management/snmp.acl.template
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/meta-index
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/net.properties
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/LucidaSansDemiOblique.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/LucidaSansOblique.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/LucidaTypewriterBoldOblique.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/LucidaTypewriterOblique.ttf
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/oblique-fonts/fonts.dir
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/plugin.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/plugin.pack
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/psfont.properties.ja
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/psfontj2d.properties
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/resources.jar
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/rt.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/rt.pack
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/US_export_policy.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/blacklist
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/cacerts
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/java.policy
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/java.security
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/javaws.policy
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/local_policy.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/security/trusted.libraries
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/servicetag
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/servicetag/jdk_header.png
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/sound.properties
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Abidjan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Accra
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Addis_Ababa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Algiers
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Asmara
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Bamako
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Bangui
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Banjul
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Bissau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Blantyre
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Brazzaville
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Bujumbura
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Cairo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Casablanca
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Ceuta
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Conakry
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Dakar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Dar_es_Salaam
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Djibouti
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Douala
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/El_Aaiun
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Freetown
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Gaborone
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Harare
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Johannesburg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Juba
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Kampala
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Khartoum
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Kigali
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Kinshasa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Lagos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Libreville
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Lome
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Luanda
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Lubumbashi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Lusaka
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Malabo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Maputo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Maseru
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Mbabane
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Mogadishu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Monrovia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Nairobi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Ndjamena
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Niamey
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Nouakchott
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Ouagadougou
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Porto-Novo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Sao_Tome
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Tripoli
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Tunis
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Africa/Windhoek
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Adak
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Anchorage
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Anguilla
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Antigua
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Araguaina
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Buenos_Aires
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Catamarca
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Cordoba
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Jujuy
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/La_Rioja
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Mendoza
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Rio_Gallegos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Salta
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/San_Juan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/San_Luis
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Tucuman
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Argentina/Ushuaia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Aruba
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Asuncion
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Atikokan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Bahia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Bahia_Banderas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Barbados
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Belem
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Belize
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Blanc-Sablon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Boa_Vista
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Bogota
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Boise
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cambridge_Bay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Campo_Grande
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cancun
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Caracas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cayenne
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cayman
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Chicago
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Chihuahua
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Costa_Rica
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Creston
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Cuiaba
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Curacao
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Danmarkshavn
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Dawson
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Dawson_Creek
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Denver
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Detroit
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Dominica
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Edmonton
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Eirunepe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/El_Salvador
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Fortaleza
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Glace_Bay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Godthab
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Goose_Bay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Grand_Turk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Grenada
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Guadeloupe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Guatemala
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Guayaquil
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Guyana
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Halifax
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Havana
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Hermosillo
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Indianapolis
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Knox
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Marengo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Petersburg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Tell_City
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Vevay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Vincennes
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Indiana/Winamac
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Inuvik
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Iqaluit
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Jamaica
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Juneau
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Kentucky
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Kentucky/Louisville
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Kentucky/Monticello
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/La_Paz
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Lima
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Los_Angeles
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Maceio
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Managua
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Manaus
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Martinique
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Matamoros
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Mazatlan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Menominee
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Merida
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Metlakatla
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Mexico_City
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Miquelon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Moncton
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Monterrey
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Montevideo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Montreal
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Montserrat
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Nassau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/New_York
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Nipigon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Nome
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Noronha
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/North_Dakota
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/North_Dakota/Beulah
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/North_Dakota/Center
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/North_Dakota/New_Salem
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Ojinaga
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Panama
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Pangnirtung
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Paramaribo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Phoenix
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Port-au-Prince
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Port_of_Spain
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Porto_Velho
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Puerto_Rico
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Rainy_River
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Rankin_Inlet
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Recife
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Regina
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Resolute
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Rio_Branco
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Santa_Isabel
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Santarem
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Santiago
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Santo_Domingo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Sao_Paulo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Scoresbysund
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Sitka
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Johns
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Kitts
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Lucia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Thomas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/St_Vincent
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Swift_Current
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Tegucigalpa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Thule
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Thunder_Bay
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Tijuana
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Toronto
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Tortola
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Vancouver
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Whitehorse
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Winnipeg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Yakutat
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/America/Yellowknife
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Casey
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Davis
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/DumontDUrville
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Macquarie
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Mawson
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/McMurdo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Palmer
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Rothera
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Syowa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Antarctica/Vostok
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Aden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Almaty
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Amman
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Anadyr
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Aqtau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Aqtobe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Ashgabat
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Baghdad
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Bahrain
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Baku
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Bangkok
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Beirut
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Bishkek
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Brunei
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Choibalsan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Chongqing
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Colombo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Damascus
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Dhaka
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Dili
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Dubai
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Dushanbe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Gaza
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Harbin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Hebron
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Ho_Chi_Minh
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Hong_Kong
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Hovd
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Irkutsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Jakarta
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Jayapura
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Jerusalem
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kabul
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kamchatka
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Karachi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kashgar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kathmandu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kolkata
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Krasnoyarsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kuala_Lumpur
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kuching
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Kuwait
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Macau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Magadan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Makassar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Manila
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Muscat
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Nicosia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Novokuznetsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Novosibirsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Omsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Oral
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Phnom_Penh
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Pontianak
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Pyongyang
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Qatar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Qyzylorda
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Rangoon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Riyadh
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Riyadh87
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Riyadh88
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Riyadh89
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Sakhalin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Samarkand
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Seoul
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Shanghai
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Singapore
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Taipei
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Tashkent
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Tbilisi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Tehran
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Thimphu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Tokyo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Ulaanbaatar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Urumqi
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Vientiane
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Vladivostok
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Yakutsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Yekaterinburg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Asia/Yerevan
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Azores
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Bermuda
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Canary
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Cape_Verde
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Faroe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Madeira
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Reykjavik
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/South_Georgia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/St_Helena
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Atlantic/Stanley
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Adelaide
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Brisbane
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Broken_Hill
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Currie
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Darwin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Eucla
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Hobart
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Lindeman
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Lord_Howe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Melbourne
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Perth
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Australia/Sydney
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/CET
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/CST6CDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/EET
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/EST
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/EST5EDT
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+1
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+10
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+11
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+12
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+2
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+3
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+4
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+5
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+6
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+7
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+8
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT+9
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-1
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-10
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-11
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-12
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-13
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-14
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-2
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-3
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-4
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-5
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-6
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-7
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-8
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/GMT-9
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/UCT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Etc/UTC
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Amsterdam
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Andorra
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Athens
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Belgrade
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Berlin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Brussels
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Bucharest
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Budapest
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Chisinau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Copenhagen
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Dublin
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Gibraltar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Helsinki
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Istanbul
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Kaliningrad
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Kiev
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Lisbon
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/London
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Luxembourg
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Madrid
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Malta
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Minsk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Monaco
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Moscow
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Oslo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Paris
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Prague
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Riga
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Rome
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Samara
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Simferopol
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Sofia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Stockholm
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Tallinn
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Tirane
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Uzhgorod
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Vaduz
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Vienna
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Vilnius
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Volgograd
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Warsaw
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Zaporozhye
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Europe/Zurich
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/GMT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/HST
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Antananarivo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Chagos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Christmas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Cocos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Comoro
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Kerguelen
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Mahe
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Maldives
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Mauritius
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Mayotte
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Indian/Reunion
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/MET
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/MST
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/MST7MDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/PST8PDT
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Apia
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Auckland
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Chatham
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Chuuk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Easter
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Efate
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Enderbury
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Fakaofo
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Fiji
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Funafuti
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Galapagos
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Gambier
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Guadalcanal
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Guam
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Honolulu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Johnston
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Kiritimati
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Kosrae
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Kwajalein
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Majuro
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Marquesas
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Midway
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Nauru
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Niue
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Norfolk
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Noumea
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Pago_Pago
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Palau
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Pitcairn
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Pohnpei
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Port_Moresby
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Rarotonga
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Saipan
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Tahiti
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Tarawa
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Tongatapu
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Wake
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/Pacific/Wallis
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/AST4
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/AST4ADT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/CST6
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/CST6CDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/EST5
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/EST5EDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/HST10
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/MST7
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/MST7MDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/PST8
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/PST8PDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/YST9
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/SystemV/YST9YDT
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/WET
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/lib/zi/ZoneInfoMappings
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/desktop
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/desktop/sun_java.desktop
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/jre/plugin/desktop/sun_java.png
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/ct.sym
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/dt.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/htmlconverter.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/ir.idl
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/jconsole.jar
%attr(0755,root,root) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/jexec
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/orb.idl
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/sa-jdi.jar
%ghost %verify(group user mode rdev) /usr/java/jdk1.6.0_45/lib/tools.jar
%config(missingok) %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/tools.pack
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/etc
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/etc/visualvm.clusters
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/etc/visualvm.conf
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/.lastModified
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/VERSION.txt
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-netbeans-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-netbeans-modules-options-api.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-netbeans-modules-queries.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-explorer.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-loaders.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-modules.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-text.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/ModuleAutoDeps/org-openide-util.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-api-annotations-common.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-api-progress.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-api-visual.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-io-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-multiview.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-output2.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core-windows.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-applemenu.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-autoupdate-services.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-autoupdate-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-core-kit.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-editor-mimelookup-impl.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-editor-mimelookup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-favorites.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-javahelp.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-keyring-impl.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-keyring.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-masterfs.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-options-api.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-options-keymap.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-print.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-progress-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-queries.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-sendopts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-settings.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-modules-spi-actions.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-spi-quicksearch.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-swing-outline.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-swing-plaf.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-netbeans-swing-tabcontrol.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-actions.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-awt.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-compat.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-dialogs.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-explorer.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-io.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-loaders.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-nodes.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-options.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-text.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-util-enumerations.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/config/Modules/org-openide-windows.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/core.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale/core_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale/core_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale/org-openide-filesystems_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/locale/org-openide-filesystems_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/core/org-openide-filesystems.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/docs
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/boot.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/boot_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/boot_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-modules_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-modules_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-util-lookup_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-util-lookup_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-util_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/locale/org-openide-util_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/nbexec
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/org-openide-modules.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/org-openide-util-lookup.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/lib/org-openide-util.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/jh-2.0_05.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/locale/updater_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/locale/updater_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/ext/updater.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-annotations-common_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-annotations-common_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-progress_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-progress_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-visual_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-api-visual_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-execution_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-execution_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-io-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-io-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-multiview_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-multiview_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-output2_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-output2_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-windows_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core-windows_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-core_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-applemenu_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-applemenu_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-autoupdate-services_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-autoupdate-services_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-autoupdate-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-autoupdate-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-core-kit_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-core-kit_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-editor-mimelookup-impl_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-editor-mimelookup-impl_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-editor-mimelookup_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-editor-mimelookup_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-favorites_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-favorites_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-javahelp_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-javahelp_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-keyring-impl_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-keyring-impl_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-keyring_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-keyring_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-masterfs_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-masterfs_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-options-api_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-options-api_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-options-keymap_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-options-keymap_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-print_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-print_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-progress-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-progress-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-queries_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-queries_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-sendopts_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-sendopts_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-settings_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-settings_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-spi-actions_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-spi-actions_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-templates_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-modules-templates_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-spi-quicksearch_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-spi-quicksearch_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-outline_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-outline_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-plaf_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-plaf_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-tabcontrol_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-netbeans-swing-tabcontrol_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-actions_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-actions_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-awt_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-awt_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-compat_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-compat_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-dialogs_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-dialogs_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-execution_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-execution_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-explorer_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-explorer_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-io_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-io_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-loaders_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-loaders_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-nodes_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-nodes_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-options_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-options_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-text_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-text_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-util-enumerations_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-util-enumerations_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-windows_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/locale/org-openide-windows_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-api-annotations-common.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-api-progress.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-api-visual.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-execution.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-io-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-multiview.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-output2.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core-windows.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-core.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-applemenu.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-autoupdate-services.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-autoupdate-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-core-kit.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-editor-mimelookup-impl.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-editor-mimelookup.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-favorites.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-javahelp.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-keyring-impl.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-keyring.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-masterfs.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-options-api.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-options-keymap.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-print.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-progress-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-queries.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-sendopts.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-settings.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-modules-spi-actions.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-spi-quicksearch.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-swing-outline.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-swing-plaf.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-netbeans-swing-tabcontrol.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-actions.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-awt.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-compat.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-dialogs.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-execution.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-explorer.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-io.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-loaders.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-nodes.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-options.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-text.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-util-enumerations.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/modules/org-openide-windows.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-api-annotations-common.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-api-progress.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-api-visual.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-bootstrap.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-io-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-multiview.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-output2.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-startup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core-windows.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-applemenu.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-autoupdate-services.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-autoupdate-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-core-kit.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-editor-mimelookup-impl.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-editor-mimelookup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-favorites.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-javahelp.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-keyring-impl.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-keyring.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-masterfs.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-options-api.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-options-keymap.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-print.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-progress-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-queries.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-sendopts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-settings.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-modules-spi-actions.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-spi-quicksearch.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-swing-outline.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-swing-plaf.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-netbeans-swing-tabcontrol.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-actions.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-awt.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-compat.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-dialogs.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-execution.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-explorer.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-filesystems.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-io.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-loaders.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-modules.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-nodes.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-options.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-text.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-util-enumerations.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-util-lookup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-util.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/platform/update_tracking/org-openide-windows.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/.lastModified
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/VERSION.txt
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-lib-profiler-charts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-lib-profiler-common.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-lib-profiler-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-lib-profiler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-modules-profiler-oql.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/config/Modules/org-netbeans-modules-profiler.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk15
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk15/linux-amd64
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk15/linux-amd64/libprofilerinterface.so
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk16
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk16/linux-amd64
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/deployed/jdk16/linux-amd64/libprofilerinterface.so
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/jfluid-server-15.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/jfluid-server.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/locale/jfluid-server_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/lib/locale/jfluid-server_zh_CN.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-charts_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-charts_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-common_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-common_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-ui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler-ui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-lib-profiler_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-modules-profiler-oql_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-modules-profiler-oql_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-modules-profiler_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/locale/org-netbeans-modules-profiler_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-lib-profiler-charts.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-lib-profiler-common.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-lib-profiler-ui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-lib-profiler.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-modules-profiler-oql.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/modules/org-netbeans-modules-profiler.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-lib-profiler-charts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-lib-profiler-common.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-lib-profiler-ui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-lib-profiler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-modules-profiler-oql.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/profiler/update_tracking/org-netbeans-modules-profiler.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/.lastModified
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-api-caching.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-application-views.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-application.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-attach.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-charts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-coredump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-heapdump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-host-remote.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-host-views.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-host.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-jmx.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-jvm.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-jvmstat.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-modules-appui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-profiler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-profiling.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-sa.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-sampler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-threaddump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-tools.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/com-sun-tools-visualvm-uisupport.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-api-visual.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-core-execution.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-core-output2.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-modules-core-kit.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-modules-favorites.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-modules-options-keymap.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-netbeans-modules-spi-actions.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-openide-compat.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-openide-options.xml_hidden
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/config/Modules/org-openide-util-enumerations.xml_hidden
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/com-sun-tools-visualvm-modules-startup.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/.svn_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/.svn_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/com-sun-tools-visualvm-modules-startup_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/com-sun-tools-visualvm-modules-startup_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/core/locale/core_visualvm.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/all-wcprops
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-api-caching.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-application-views.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-application.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-attach.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-charts.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-core.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-coredump.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-heapdump.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-host-remote.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-host-views.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-host.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-jmx.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-jvm.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-jvmstat.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-modules-appui.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-profiler.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-profiling.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-sa.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-sampler.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-threaddump.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-tools.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/com-sun-tools-visualvm-uisupport.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/entries
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-api-caching_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-api-caching_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-application-views_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-application-views_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-application_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-application_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-attach_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-attach_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-charts_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-charts_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-core_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-core_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-coredump_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-coredump_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-heapdump_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-heapdump_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host-remote_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host-remote_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host-views_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host-views_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-host_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jmx_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jmx_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jvm_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jvm_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jvmstat_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-jvmstat_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-modules-appui_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-modules-appui_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-profiler_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-profiler_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-profiling_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-profiling_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-sa_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-sa_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-sampler_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-sampler_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-threaddump_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-threaddump_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-tools_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-tools_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-uisupport_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/com-sun-tools-visualvm-uisupport_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-core-windows_visualvm.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-core_visualvm.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-.svn_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-.svn_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-profiler_visualvm.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-prop-base_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-prop-base_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-props_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-props_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-text-base_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-text-base_zh_CN.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-tmp_ja.jar
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/modules/locale/org-netbeans-modules-tmp_zh_CN.jar
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-api-caching.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-application-views.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-application.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-attach.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-charts.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-core.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-coredump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-heapdump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-host-remote.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-host-views.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-host.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-jmx.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-jvm.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-jvmstat.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-modules-appui.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-modules-startup.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-profiler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-profiling.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-sa.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-sampler.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-threaddump.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-tools.xml
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/lib/visualvm/visualvm/update_tracking/com-sun-tools-visualvm-uisupport.xml
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/appletviewer.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/apt.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/extcheck.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/idlj.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jar.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jarsigner.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/java.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/javac.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/javadoc.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/javah.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/javap.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jconsole.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jdb.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jhat.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jinfo.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jmap.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jps.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jrunscript.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jsadebugd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jstack.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jstat.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jstatd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/jvisualvm.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/keytool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/native2ascii.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/orbd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/pack200.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/policytool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/rmic.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/rmid.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/rmiregistry.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/schemagen.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/serialver.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/servertool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/tnameserv.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/unpack200.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/wsgen.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/wsimport.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/ja_JP.eucJP/man1/xjc.1
%dir %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/appletviewer.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/apt.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/extcheck.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/idlj.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jar.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jarsigner.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/java.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javac.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javadoc.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javah.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javap.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/javaws.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jconsole.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jdb.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jhat.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jinfo.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jmap.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jps.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jrunscript.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jsadebugd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jstack.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jstat.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jstatd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/jvisualvm.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/keytool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/native2ascii.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/orbd.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/pack200.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/policytool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/rmic.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/rmid.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/rmiregistry.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/schemagen.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/serialver.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/servertool.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/tnameserv.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/unpack200.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/wsgen.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/wsimport.1
%doc %verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/man/man1/xjc.1
%verify(group md5 size link mtime user mode rdev) /usr/java/jdk1.6.0_45/src.zip




%post -p /bin/sh
#
    # Make sure any new files are created with a secure access mask.  Do not use
    # chmod, since that would also change the rights of any existing files, and
    # we are only interested in setting the rights for new files.
    #
    umask 022

    #
    # The package assumes that Gnome is either installed, or going to be
    # installed, so if nothing currently exists, then install in the default
    # location.
    #
    # NOTE: These variables must be defined before all the shell function macros
    #       are included.
    #
    if [ -z "${GNOMEDIR}" ]; then
        GNOMEDIR=/usr
    fi

    #
    # RPM_INSTALL_PREFIX doesn't seem to be set by "alien" so the following
    # minor kludge allows some functionality on debian-like systems (such
    # a Ubuntu) which don't support packages.
    #
    if [ -z "${RPM_INSTALL_PREFIX}" ]; then
	RPM_INSTALL_PREFIX="/usr/java"
    fi

    #
    # Gross kludge for old SuSE distros: Even though they set the environment
    # variable GNOMEDIR to /opt/gnome, Gnome may really be in /opt/gnome2.
    # Go figure,... (I feel so unclean....)
    #
    if [ "${GNOMEDIR}" = "/opt/gnome" ] && [ -d "/opt/gnome2" ]; then
	GNOMEDIR="/opt/gnome2"
    fi

    INSTALL_JRE_PATH=${RPM_INSTALL_PREFIX}/jdk1.6.0_45
    if [ -e ${INSTALL_JRE_PATH}/jre/bin/java ]; then
	INSTALL_JRE_PATH=${INSTALL_JRE_PATH}/jre
    fi

    #
    # Add the shell function and related variables used by the post-install.
    #
    ERROR_MISSING_PARAM=1000
ERROR_MISSING_PACKED_JAR=1001
ERROR_BAD_PARAM=1002
ERROR_MISSING_UNPACK200=1003
unpack_jars() {
    status=0
    if [ $# -lt 3 ]; then
        printf "Error: usage - no packed files specified, nothing to do:\n\n" \
								>> /dev/stderr
        printf "\t unpack_jars\n" "$*"                          >> /dev/stderr
        status=${ERROR_MISSING_PARAM}
    else
        unpack200=$1
        root=$2
        shift 2
        if [ -f ${unpack200} ]; then
            if [ -d ${root} ]; then                
                printf "Unpacking JAR files...\n"
                for file in $*; do
                    pack_file=`basename ${file} .jar`.pack
                    pack_src=${root}/`dirname ${file}`/${pack_file}
                    jar_dest=${root}/${file}
                    printf "\t%s...\n" "`basename ${file}`"
                    ${unpack200} ${pack_src} ${jar_dest}
                    if [ ! -f ${jar_dest} ]; then
                        printf "Error: unpack could not create JAR file:\n\n" \
								>> /dev/stderr
                        printf "\t%s\n\n" "${jar_dest}"		>> /dev/stderr
                        printf "Please refer to the "		>> /dev/stderr
			printf "Troubleshooting section of "    >> /dev/stderr
                        printf "the Installation "              >> /dev/stderr
                        printf "Instructions\n"                 >> /dev/stderr
                        printf "on the download page.\n"        >> /dev/stderr
                        status=${ERROR_MISSING_PACKED_JAR}
                    fi
                    rm -f ${pack_src}
                done
            else
                printf "Error: usage - the base path for the "  >> /dev/stderr
                printf "packed JAR files is invalid:\n\n"	>> /dev/stderr
                printf "\tunpack_jars %s\n" "$*"		>> /dev/stderr
                status=${ERROR_BAD_PARAM}
            fi
        else
            printf "Error: unpack200 - command could not be found.\n\n" \
								>> /dev/stderr
            printf "Please refer to the Troubleshooting "       >> /dev/stderr
            printf "section of the"                             >> /dev/stderr
            printf "Installation Instructions\n"                >> /dev/stderr
            printf "on the download page.\n"                    >> /dev/stderr
            status=${ERROR_MISSING_UNPACK200}
        fi
    fi
    return ${status}
}
    NS_COMMENT1="#--Netscape Communications Corporation MIME Information"
NS_COMMENT2="#Do not delete the above line. It is used to identify the file type."
NS_COMMENT3="#mime types added by Netscape Helper"
UpdateMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    command="$3"
    if [ -z "`grep -E \"^${mime_type}; ${command}$\" \"${mailcap_file}\" 2> /dev/null`" ]; then
        mc_comment="# Java Web Start"
        mc_text=
        if [ -w "${mailcap_file}" ]; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
        fi
        if [ -w "`dirname \"${mailcap_file}\"`" ]; then
            mc_text="${mc_text:+${mc_text}\n}${mime_type}; ${command}"
            printf "%s" "${mc_text}" > "${mailcap_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mailcap_file}"
            echo "Check permissions."
        fi
    fi
}
RemoveMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    mc_comment="# Java Web Start"
    if [ -w "${mailcap_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mailcap_file}\"`" ] ; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
            if [ `echo "${mc_text}" | tr -d '[:space:]' | wc -c` -gt 0 ]; then
                echo "${mc_text}" > "${mailcap_file}"
            else
                rm -f "${mailcap_file}"
            fi
        fi
    fi
}
UpdateMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    desc="$3"
    shift 3
    exts="$*"
    JNLP_ENTRY="type=${mime_type} desc=\"${desc}\" exts=\"${exts}\""
    if [ ! -w "${mime_file}" ]; then
        if [ -w `dirname ${mime_file}` ]; then
            echo "${NS_COMMENT1}"  > "${mime_file}"
            echo "${NS_COMMENT2}" >> "${mime_file}"
            echo "${NS_COMMENT3}" >> "${mime_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mime_file}"
            echo "Check permissions."
            return
        fi
    fi
    if [ -z "`grep -E \"^[^#]*${mime_type}\" \"${mime_file}\"`" ]; then
        echo ${JNLP_ENTRY} >> "${mime_file}"
    fi
}
RemoveMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    if [ -w "${mime_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mime_file}\"`" ]; then
            regexp="(${mime_type})|(^${NS_COMMENT1}$)|(^${NS_COMMENT2}$)|(^${NS_COMMENT3}$)"
            if [ `grep -Ev "${regexp}" "${mime_file}" | \
                 tr -d '[:space:]' | wc -c` -gt 0 ]
            then
                mt_text="`grep -v \"${mime_type}\" \"${mime_file}\"`"
                echo "${mt_text}" > "${mime_file}"
            else
                rm -f "${mime_file}"
            fi
        fi
    fi
}
    MOST_DIGITS="[1-9]"
ALL_DIGITS="[0-9]"
COUNTING_NUMBER="${MOST_DIGITS}${ALL_DIGITS}*\|0"
VALID_NON_NUMERIC="[-_.a-zA-Z]"
VALID_CHARS="[-_.a-zA-Z0-9]"
MAJOR_RULE="\(${MOST_DIGITS}${ALL_DIGITS}*\)"
MINOR_RULE="\(${COUNTING_NUMBER}\)"
MICRO_RULE="\(${COUNTING_NUMBER}\)"
UPDATE_RULE="\(${MOST_DIGITS}${ALL_DIGITS}\|0${ALL_DIGITS}\)"
NON_FCS_ID_RULE="\([a-zA-Z0-9]*\)"
MIN_VERSION_ID_RULE="${MAJOR_RULE}\.${MINOR_RULE}\.${MICRO_RULE}"
FCS_VERSION_ID_RULE="${MIN_VERSION_ID_RULE}\(_${UPDATE_RULE}\)\?"
VERSION_ID_RULE="${FCS_VERSION_ID_RULE}\(-${NON_FCS_ID_RULE}\)\?"
NAME_ID_RULE="${VALID_CHARS}*${VALID_NON_NUMERIC}"
KNOWN_GOOD_NAME_LIST="java jdk jre j2sdk j2re"
PRS_ERROR_BAD_PARAMS=2000
expand_version() {
    status=0
    if [ $# -eq 0 ]; then
        read release remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${release}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${release}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        release=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        \printf "\t expand_version\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        format="%d\t%d\t%d\t%d\n"
        echo ${release} | sed -e "s/_/\./g" | \
          awk -v format="${format}" 'BEGIN { FS = "." } { printf format, $1, $2, $3, $4 }'
    fi
    return ${status}
}
parse_release() {
    status=0
    if [ $# -eq 0 ]; then
        read string remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${string}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${string}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        string=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t parse_release %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        version_id=`expr "${string}" : "${NAME_ID_RULE}\(${VERSION_ID_RULE}\)\$"`
        if [ -n "${version_id}" ]; then
            name_id=`expr "${string}" : "\(${NAME_ID_RULE}\)${VERSION_ID_RULE}\$"`
            fcs_part=`expr "${string}" : "${NAME_ID_RULE}\(${FCS_VERSION_ID_RULE}\).*\$"`
            non_fcs_part=`expr "${version_id}" : "[^-]*-\(${NON_FCS_ID_RULE}\)\$"`
	    printf "%s\t%s\t%s\n" "${name_id}" "${fcs_part}" "${non_fcs_part}"
        fi
    fi
    return ${status}
}
UNKNOWN_NAME_WEIGHT=1000
get_name_weight() {
    status=0
    if [ "$1" = "-" ]; then
        read name good_names
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        else
            shift 1
            if [ $# -gt 0 ]; then
                good_names="$*"
            fi
            if [ -z "${name}" ]; then
                printf "Error: usage - function requires input!\n" >> /dev/stderr
                status=${PRS_ERROR_BAD_PARAMS}
            fi
        fi
    elif [ $# -gt 1 ]; then
        name=$1
        shift 1
        good_names="$*"
    else
        printf "Error: usage - function takes 2+ parameters:\n\n" >> /dev/stderr
        printf "\t get_name_weight %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -n "${good_names}" ]; then
            length=`expr length "${good_names}"`
            pos=`expr "${good_names}" : ".*\<${name}\>"`
            if [ ${pos} -gt 0 ]; then
                expr substr "${good_names}" 1 ${pos} | wc -w | tr -d "[:space:]"
            else
                echo ${UNKNOWN_NAME_WEIGHT}
            fi
        else
            echo ${UNKNOWN_NAME_WEIGHT}
        fi
    fi
    return ${status}
}
HAS_FCS_WEIGHT=0
HAS_ODD_FCS_WEIGHT=1
HAS_RC_WEIGHT=100
HAS_ODD_RC_WEIGHT=101
HAS_BETA_WEIGHT=300
HAS_ODD_BETA_WEIGHT=301
HAS_EA_WEIGHT=500
HAS_ODD_EA_WEIGHT=501
HAS_INTRNAL_WEIGHT=2000
HAS_VERY_ODD_WEIGHT=9999
get_non_fcs_weight() {
    status=0
    if [ $# -eq 0 ]; then
        read non_fcs_part remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${non_fcs_part}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        non_fcs_part=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t get_non_fcs_weight \n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -z "${non_fcs_part}" ]; then
            echo ${HAS_FCS_WEIGHT}
        else
            case "${non_fcs_part}" in
                fcs)
                    echo ${HAS_ODD_FCS_WEIGHT}
                    ;;
                rc)
                    echo ${HAS_RC_WEIGHT}
                    ;;
                rc[0-9] | rc[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "rc\([0-9]*\)$"`
                    echo `expr ${HAS_RC_WEIGHT} - ${count}`
                    ;;
                rc*)
                    echo ${HAS_ODD_RC_WEIGHT}
                    ;;
                beta)
                    echo ${HAS_BETA_WEIGHT}
                    ;;
                beta[0-9] | beta[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "beta\([0-9]*\)$"`
                    echo `expr ${HAS_BETA_WEIGHT} - ${count}`
                    ;;
                beta*)
                    echo ${HAS_ODD_BETA_WEIGHT}
                    ;;
                ea)
                    echo ${HAS_EA_WEIGHT}
                    ;;
                ea[0-9] | ea[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "ea\([0-9]*\)$"`
                    echo `expr ${HAS_EA_WEIGHT} - ${count}`
                    ;;
                ea*)
                    echo ${HAS_ODD_EA_WEIGHT}
                    ;;
                internal)
                    echo ${HAS_INTRNAL_WEIGHT}
                    ;;
                internal[0-9] | internal[0-9][0-9] | internal[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "internal\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                b[0-9] | b[0-9][0-9] | b[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "b\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                *)
                    echo ${HAS_VERY_ODD_WEIGHT}
                    ;;
            esac
        fi
    fi
    return ${status}
}
    get_path_weight() {
    good_list="$1"
    path=$2
    release=`basename ${path}`
    parts="`parse_release ${release}`"
    if [ $? -eq 0 ]; then
        name=`echo "${parts}" | cut -f1`
        version=`echo "${parts}" | cut -f2`
        non_fcs=`echo "${parts}" | cut -f3`
        if [ -n "${version}" ]; then
           v_weight=`echo ${version} | expand_version`
           n_weight=`echo ${name} | get_name_weight - "${good_list}"`
           o_weight=`echo ${non_fcs} | get_non_fcs_weight`
           printf "%4d  %4d  %4d  %4d  %4d  %4d  %s\n" \
                  ${v_weight} ${n_weight} ${o_weight} "${path}"
        fi
    fi
}
get_weighted_list() {
    good_list=
    verify=
    stdio=
    status=0
    check=true
    while [ -n "${check}" ]; do
        if [ $# -gt 0 ]; then
            case "$1" in
                -g)
                    good_list="$2"
                    shift 2
                    ;;
                --good-list=*)
                    length=`expr length "$1"`
                    remove=`expr \( length "--good-list=" \) + 1`
                    good_list="`expr substr \"$1\" ${remove} ${length}`"
                    shift 1
                    ;;
                -v | --verify)
                    verify=true
                    shift 1
                    ;;
                --)
                    shift 1
                    check=
                    ;;
                -)
                    shift 1
                    stdio=true
                    ;;
                -*)
                    printf "Error: usage - unknown parameter:\n\n" \
								>> /dev/stderr
                    printf "\t%s : %s\n" "$1" "$*"		>> /dev/stderr
                    status=${PRS_ERROR_BAD_PARAMS}
                    check=
                    ;;
                *)
                    check=
                    ;;
            esac
        else
            check=
        fi
    done
    if [ $# -eq 0 ] || [ -n "${stdio}" ]; then
        read line
        while [ -n "${line}" ]; do
            if [ -z "${verify}" ] || [ -f ${line}/bin/java ]; then
                get_path_weight "${good_list}" ${line}
            fi
            read line
        done
    fi
    while [ $# -gt 0 ]; do
        if [ -z "${verify}" ] || [ -f $1/bin/java ]; then
            get_path_weight "${good_list}" $1
        fi
        shift 1
    done
    return ${status}
}
_compare_java_by_weight() {
    compare=0
    if [ $# -ne 0 ]; then
        if [ $# -eq 1 ]; then
            compare=1
        else
            left=$1
            right=$2
            shift 2
            good="$*"
            list=`get_weighted_list --good-list="${good}" \
                    ${left} ${right} | sort -u -k1n -k2n -k3n -k4n -k5rn -k6rn`
            if [ `echo "${list}" | wc -l | tr -d "[:space:]"` -ne 1 ]; then
                compare=-1
                latest=`echo "${list}" | tail -n 1 | cut -c 37-`
                if [ "${left}" = "${latest}" ]; then
                    compare=1
                fi
            fi
        fi
    fi
    echo ${compare}
}
compare_java_by_version() {
    _compare_java_by_weight $1 $2
}
compare_java_by_release() {
    _compare_java_by_weight $1 $2 ${KNOWN_GOOD_NAME_LIST}
}
find_latest_release() {
    if [ -d /usr/java ]; then
        latest_release=`find /usr/java/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
    fi
    if [ -d "${RPM_INSTALL_PREFIX}" ] && \
       [ "/usr/java" != "${RPM_INSTALL_PREFIX}" ]
    then 
        prefix_release=`find ${RPM_INSTALL_PREFIX}/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
        if [ `compare_java_by_release ${latest_release} ${prefix_release}` -lt 0 ]; then
            latest_release=${prefix_release}
        fi
    fi
    echo ${latest_release}
}
get_javaws() {
    path=$1
    if [ `compare_java_by_version ${path} version-1.5.0` -ge 0 ] &&
       [ -f ${path}/bin/javaws ]
    then
        path=${path}/bin/javaws
    elif [ `compare_java_by_version ${path} version-1.4.2` -ge 0 ]; then
        if [ -f ${path}/jre/javaws/javaws ]; then
            path=${path}/jre/javaws/javaws
        elif [ -f ${path}/javaws/javaws ]; then
            path=${path}/javaws/javaws
        else
            path=
        fi
    else
        path=
    fi
    echo ${path}
}
    LINK_ERROR_BAD_PARAMS=3000
LINK_ERROR_DEAD_LINK=3001
LINK_ERROR_FILE_NOT_FOUND=3002
dereference() {
    status=0
    if [ "$1" = "-f" ] || [ "$1" = "--follow" ]; then
        follow="--follow"
        shift 1
    fi
    if [ $# -ge 1 ]; then
        path="$*"
        if [ -e "${path}" ]; then
            parent="`cd \`dirname \"${path}\"\`; pwd`"
            child="`basename \"${path}\"`"
            if [ "${parent}" != "${child}" ]; then
                path="${parent}/${child}"
            fi
            if [ -h "${path}" ]; then
                path=`ls -l "${path}" | sed -e "s#^.*${path} -> ##"`
                if [ "`expr substr \"${path}\" 1 1`" != "/" ]; then
                    path="${parent}/${path}"
                fi
                if [ -n "${follow}" ]; then
                    path="`dereference ${follow} ${path}`"
                fi                    
            fi
        else
            status=${LINK_ERROR_FILE_NOT_FOUND}
        fi
    fi
    echo ${path}
    return ${status}
}
setup_latest_link() {
    latest=$1
    link=$2
    if [ -h "${link}" ]; then
        reference="`dereference --follow ${link}`"
        if [ $? -eq 0 ]; then
            update=`compare_java_by_release "${latest}" "${reference}"`
        else
            update=1
        fi
        if [ ${update} -gt 0 ]; then
            rm -f "${link}"
        fi
    fi
    if [ ! -e "${link}" ]; then
        ln -s "${latest}" "${link}"
    fi
}
setup_default_links() {
    if [ $# -ge 2 ]; then
        latest_link="$1"
        default_link="$2"
        if [ ! -e "${default_link}" ]; then
            ln -s "${latest_link}" "${default_link}"
        fi
    fi
    if [ $# -gt 3 ]; then
        bindir="$3"
        shift 3
        for file in $*; do
            reference="`dereference --follow ${bindir}/${file}`"
            if [ $? -ne 0 ]; then
                rm -f "${bindir}/${file}"
            fi
            source="${default_link}/bin/${file}"
            if [ "${file}" = "javaws" ]; then
                source="`get_javaws \"${default_link}\"`"
            fi
            if [ -n "${source}" ] && [ ! -e "${bindir}/${file}" ]; then
                ln -s "${source}" "${bindir}/${file}"
            fi
        done
    fi
}
cleanup_default_links() {
    if [ $# -ge 1 ]; then
        default_link=$1
        if [ $# -gt 2 ]; then
            bindir="$2"
            shift 2
            for file in $*; do
                reference="`dereference \"${bindir}/${file}\"`"
                if [ $? -ne 0 ] ||
                   [ "${reference}" = "${default_link}/bin/${file}" ]
                then
                    rm -f "${bindir}/${file}"
                fi
            done
        fi
        rm -f "${default_link}"
    fi
}

    #
    # Unpack the packed JAR files.
    #
    unpack_jars "${RPM_INSTALL_PREFIX}/jdk1.6.0_45/bin/unpack200" \
                "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" \
                jre/lib/rt.jar jre/lib/jsse.jar jre/lib/charsets.jar lib/tools.jar jre/lib/ext/localedata.jar jre/lib/plugin.jar jre/lib/javaws.jar jre/lib/deploy.jar



    #
    # Find out what version of Java is the latest.  Don't do any system
    # integration unless this is the latest version.  Otherwise, we make it
    # difficult for future installers.
    #
    LATEST_JAVA_PATH="`find_latest_release`"
    if [ "${LATEST_JAVA_PATH}" == "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ] ||
       [ "${LATEST_JAVA_PATH}" == "/usr/java/jdk1.6.0_45" ]
    then
        #
        # Make sure the /usr/java/latest link points to LATEST_JAVA_PATH, and
	# update it if it doesn't.
        #
        setup_latest_link "${LATEST_JAVA_PATH}" "/usr/java/latest"

        #
        # Make sure the /usr/java/default and java javaws jcontrol javac jar javadoc exist.
	# If anything is missing, create it.
        #
        setup_default_links "/usr/java/latest" "/usr/java/default" \
                            "/usr/bin" java javaws jcontrol javac jar javadoc

        #
        # If the "latest" link is a JDK, then the latest JRE is a subdir;
	# otherwise it is the same dir.
        #
        DEFAULT_JRE_PATH="/usr/java/default"
        if [ -e "/usr/java/default/jre/bin/java" ]; then
            DEFAULT_JRE_PATH="/usr/java/default/jre"
        fi

    fi

    #
    # If the package is being relocated, then create a link in the default
    # location (/usr/java) to the actual install directory.  Do this
    # last, so it doesn't add unnecessary complexity to the search for the
    # latest release.
    #
    if [ "${RPM_INSTALL_PREFIX}" != "/usr/java" ] &&
       ( [ ! -e "/usr/java/jdk1.6.0_45" ] || [ -h "/usr/java/jdk1.6.0_45" ] )
    then
        rm -f "/usr/java/jdk1.6.0_45"
        ln -s "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" "/usr/java/jdk1.6.0_45"
    fi

    #
    # Next, make sure the files required for the Prferences API are setup
    # correctly.  Any files from an old, uninstalled version will have left
    # files with a .rpmsave extension.  If there was an older version currently
    # installed when this version installed, there will be a set of files with
    # a .rpmnew extension.  Try to use the best possible file (i.e. save old
    # preference settings).
    #
    if [ -f /etc/.java/.systemPrefs/.system.lock.rpmsave ] &&
       [ ! -s /etc/.java/.systemPrefs/.system.lock ]
    then
        #
        # Only overwrite if old file is empty (rpmsave is only created if it is
        # non-empty).
        #
        rm -f /etc/.java/.systemPrefs/.system.lock
        mv /etc/.java/.systemPrefs/.system.lock.rpmsave \
           /etc/.java/.systemPrefs/.system.lock
    elif [ -f /etc/.java/.systemPrefs/.system.lock.rpmnew ]
    then
        if [ -s /etc/.java/.systemPrefs/.system.lock ]; then
            #
            # The existing lock is non-empty, so there is no reason to keep the
            # .rpmnew one created during this install.
            #
            rm -f /etc/.java/.systemPrefs/.system.lock.rpmnew
        else
            #
            # The existing lock is empty, so replace it with the new one.  This
            # makes future installs a little cleaner, since the file in use is
            # the file in the RPM database.
            #
            rm -f /etc/.java/.systemPrefs/.system.lock
            mv /etc/.java/.systemPrefs/.system.lock.rpmnew \
               /etc/.java/.systemPrefs/.system.lock
        fi
    fi

    if [ -f /etc/.java/.systemPrefs/.systemRootModFile.rpmsave ] &&
       [ ! -s /etc/.java/.systemPrefs/.systemRootModFile ]
    then
        #
        # Only overwrite if old file is empty (rpmsave is only created if it is
        # non-empty).
        #
        rm -f /etc/.java/.systemPrefs/.systemRootModFile
        mv /etc/.java/.systemPrefs/.systemRootModFile.rpmsave \
           /etc/.java/.systemPrefs/.systemRootModFile
    elif [ -f /etc/.java/.systemPrefs/.systemRootModFile.rpmnew ]
    then
        if [ -s /etc/.java/.systemPrefs/.systemRootModFile ]; then
            #
            # The existing lock is non-empty, so there is no reason to keep the
            # .rpmnew one created during this install.
            #
            rm -f /etc/.java/.systemPrefs/.systemRootModFile.rpmnew
        else
            #
            # The existing lock is empty, so replace it with the new one.  This
            # makes future installs a little cleaner, since the file in use is
            # the file in the RPM database.
            #
            rm -f /etc/.java/.systemPrefs/.systemRootModFile
            mv /etc/.java/.systemPrefs/.systemRootModFile.rpmnew \
               /etc/.java/.systemPrefs/.systemRootModFile
        fi
    fi

    #
    # Try to register the init script to the various run levels.  If possible
    # this is accomplished using an LSB defined install tool.  If that isn't
    # available, then try to use chkconfig, which is supported by Red Hat and
    # Debian.  The feature of automatic jar file execution is not support on
    # systems which don't support either of these interfaces.
    #
    if [ -x /usr/lib/lsb/install_initd ]; then
        /usr/lib/lsb/install_initd jexec > /dev/null 2>&1

        # start the service for the current session
        /etc/init.d/jexec start > /dev/null 2>&1
    elif [ -x /sbin/chkconfig ]; then
        /sbin/chkconfig --add jexec > /dev/null 2>&1

        # start the service for the current session
        /etc/init.d/jexec start > /dev/null 2>&1
    fi


%preun -p /bin/sh
#
    # Add the shell function and related variables used by the pre-uninstall.
    #
    MOST_DIGITS="[1-9]"
ALL_DIGITS="[0-9]"
COUNTING_NUMBER="${MOST_DIGITS}${ALL_DIGITS}*\|0"
VALID_NON_NUMERIC="[-_.a-zA-Z]"
VALID_CHARS="[-_.a-zA-Z0-9]"
MAJOR_RULE="\(${MOST_DIGITS}${ALL_DIGITS}*\)"
MINOR_RULE="\(${COUNTING_NUMBER}\)"
MICRO_RULE="\(${COUNTING_NUMBER}\)"
UPDATE_RULE="\(${MOST_DIGITS}${ALL_DIGITS}\|0${ALL_DIGITS}\)"
NON_FCS_ID_RULE="\([a-zA-Z0-9]*\)"
MIN_VERSION_ID_RULE="${MAJOR_RULE}\.${MINOR_RULE}\.${MICRO_RULE}"
FCS_VERSION_ID_RULE="${MIN_VERSION_ID_RULE}\(_${UPDATE_RULE}\)\?"
VERSION_ID_RULE="${FCS_VERSION_ID_RULE}\(-${NON_FCS_ID_RULE}\)\?"
NAME_ID_RULE="${VALID_CHARS}*${VALID_NON_NUMERIC}"
KNOWN_GOOD_NAME_LIST="java jdk jre j2sdk j2re"
PRS_ERROR_BAD_PARAMS=2000
expand_version() {
    status=0
    if [ $# -eq 0 ]; then
        read release remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${release}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${release}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        release=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        \printf "\t expand_version\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        format="%d\t%d\t%d\t%d\n"
        echo ${release} | sed -e "s/_/\./g" | \
          awk -v format="${format}" 'BEGIN { FS = "." } { printf format, $1, $2, $3, $4 }'
    fi
    return ${status}
}
parse_release() {
    status=0
    if [ $# -eq 0 ]; then
        read string remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${string}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${string}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        string=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t parse_release %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        version_id=`expr "${string}" : "${NAME_ID_RULE}\(${VERSION_ID_RULE}\)\$"`
        if [ -n "${version_id}" ]; then
            name_id=`expr "${string}" : "\(${NAME_ID_RULE}\)${VERSION_ID_RULE}\$"`
            fcs_part=`expr "${string}" : "${NAME_ID_RULE}\(${FCS_VERSION_ID_RULE}\).*\$"`
            non_fcs_part=`expr "${version_id}" : "[^-]*-\(${NON_FCS_ID_RULE}\)\$"`
	    printf "%s\t%s\t%s\n" "${name_id}" "${fcs_part}" "${non_fcs_part}"
        fi
    fi
    return ${status}
}
UNKNOWN_NAME_WEIGHT=1000
get_name_weight() {
    status=0
    if [ "$1" = "-" ]; then
        read name good_names
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        else
            shift 1
            if [ $# -gt 0 ]; then
                good_names="$*"
            fi
            if [ -z "${name}" ]; then
                printf "Error: usage - function requires input!\n" >> /dev/stderr
                status=${PRS_ERROR_BAD_PARAMS}
            fi
        fi
    elif [ $# -gt 1 ]; then
        name=$1
        shift 1
        good_names="$*"
    else
        printf "Error: usage - function takes 2+ parameters:\n\n" >> /dev/stderr
        printf "\t get_name_weight %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -n "${good_names}" ]; then
            length=`expr length "${good_names}"`
            pos=`expr "${good_names}" : ".*\<${name}\>"`
            if [ ${pos} -gt 0 ]; then
                expr substr "${good_names}" 1 ${pos} | wc -w | tr -d "[:space:]"
            else
                echo ${UNKNOWN_NAME_WEIGHT}
            fi
        else
            echo ${UNKNOWN_NAME_WEIGHT}
        fi
    fi
    return ${status}
}
HAS_FCS_WEIGHT=0
HAS_ODD_FCS_WEIGHT=1
HAS_RC_WEIGHT=100
HAS_ODD_RC_WEIGHT=101
HAS_BETA_WEIGHT=300
HAS_ODD_BETA_WEIGHT=301
HAS_EA_WEIGHT=500
HAS_ODD_EA_WEIGHT=501
HAS_INTRNAL_WEIGHT=2000
HAS_VERY_ODD_WEIGHT=9999
get_non_fcs_weight() {
    status=0
    if [ $# -eq 0 ]; then
        read non_fcs_part remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${non_fcs_part}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        non_fcs_part=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t get_non_fcs_weight \n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -z "${non_fcs_part}" ]; then
            echo ${HAS_FCS_WEIGHT}
        else
            case "${non_fcs_part}" in
                fcs)
                    echo ${HAS_ODD_FCS_WEIGHT}
                    ;;
                rc)
                    echo ${HAS_RC_WEIGHT}
                    ;;
                rc[0-9] | rc[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "rc\([0-9]*\)$"`
                    echo `expr ${HAS_RC_WEIGHT} - ${count}`
                    ;;
                rc*)
                    echo ${HAS_ODD_RC_WEIGHT}
                    ;;
                beta)
                    echo ${HAS_BETA_WEIGHT}
                    ;;
                beta[0-9] | beta[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "beta\([0-9]*\)$"`
                    echo `expr ${HAS_BETA_WEIGHT} - ${count}`
                    ;;
                beta*)
                    echo ${HAS_ODD_BETA_WEIGHT}
                    ;;
                ea)
                    echo ${HAS_EA_WEIGHT}
                    ;;
                ea[0-9] | ea[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "ea\([0-9]*\)$"`
                    echo `expr ${HAS_EA_WEIGHT} - ${count}`
                    ;;
                ea*)
                    echo ${HAS_ODD_EA_WEIGHT}
                    ;;
                internal)
                    echo ${HAS_INTRNAL_WEIGHT}
                    ;;
                internal[0-9] | internal[0-9][0-9] | internal[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "internal\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                b[0-9] | b[0-9][0-9] | b[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "b\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                *)
                    echo ${HAS_VERY_ODD_WEIGHT}
                    ;;
            esac
        fi
    fi
    return ${status}
}
    get_path_weight() {
    good_list="$1"
    path=$2
    release=`basename ${path}`
    parts="`parse_release ${release}`"
    if [ $? -eq 0 ]; then
        name=`echo "${parts}" | cut -f1`
        version=`echo "${parts}" | cut -f2`
        non_fcs=`echo "${parts}" | cut -f3`
        if [ -n "${version}" ]; then
           v_weight=`echo ${version} | expand_version`
           n_weight=`echo ${name} | get_name_weight - "${good_list}"`
           o_weight=`echo ${non_fcs} | get_non_fcs_weight`
           printf "%4d  %4d  %4d  %4d  %4d  %4d  %s\n" \
                  ${v_weight} ${n_weight} ${o_weight} "${path}"
        fi
    fi
}
get_weighted_list() {
    good_list=
    verify=
    stdio=
    status=0
    check=true
    while [ -n "${check}" ]; do
        if [ $# -gt 0 ]; then
            case "$1" in
                -g)
                    good_list="$2"
                    shift 2
                    ;;
                --good-list=*)
                    length=`expr length "$1"`
                    remove=`expr \( length "--good-list=" \) + 1`
                    good_list="`expr substr \"$1\" ${remove} ${length}`"
                    shift 1
                    ;;
                -v | --verify)
                    verify=true
                    shift 1
                    ;;
                --)
                    shift 1
                    check=
                    ;;
                -)
                    shift 1
                    stdio=true
                    ;;
                -*)
                    printf "Error: usage - unknown parameter:\n\n" \
								>> /dev/stderr
                    printf "\t%s : %s\n" "$1" "$*"		>> /dev/stderr
                    status=${PRS_ERROR_BAD_PARAMS}
                    check=
                    ;;
                *)
                    check=
                    ;;
            esac
        else
            check=
        fi
    done
    if [ $# -eq 0 ] || [ -n "${stdio}" ]; then
        read line
        while [ -n "${line}" ]; do
            if [ -z "${verify}" ] || [ -f ${line}/bin/java ]; then
                get_path_weight "${good_list}" ${line}
            fi
            read line
        done
    fi
    while [ $# -gt 0 ]; do
        if [ -z "${verify}" ] || [ -f $1/bin/java ]; then
            get_path_weight "${good_list}" $1
        fi
        shift 1
    done
    return ${status}
}
_compare_java_by_weight() {
    compare=0
    if [ $# -ne 0 ]; then
        if [ $# -eq 1 ]; then
            compare=1
        else
            left=$1
            right=$2
            shift 2
            good="$*"
            list=`get_weighted_list --good-list="${good}" \
                    ${left} ${right} | sort -u -k1n -k2n -k3n -k4n -k5rn -k6rn`
            if [ `echo "${list}" | wc -l | tr -d "[:space:]"` -ne 1 ]; then
                compare=-1
                latest=`echo "${list}" | tail -n 1 | cut -c 37-`
                if [ "${left}" = "${latest}" ]; then
                    compare=1
                fi
            fi
        fi
    fi
    echo ${compare}
}
compare_java_by_version() {
    _compare_java_by_weight $1 $2
}
compare_java_by_release() {
    _compare_java_by_weight $1 $2 ${KNOWN_GOOD_NAME_LIST}
}
find_latest_release() {
    if [ -d /usr/java ]; then
        latest_release=`find /usr/java/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
    fi
    if [ -d "${RPM_INSTALL_PREFIX}" ] && \
       [ "/usr/java" != "${RPM_INSTALL_PREFIX}" ]
    then 
        prefix_release=`find ${RPM_INSTALL_PREFIX}/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
        if [ `compare_java_by_release ${latest_release} ${prefix_release}` -lt 0 ]; then
            latest_release=${prefix_release}
        fi
    fi
    echo ${latest_release}
}
get_javaws() {
    path=$1
    if [ `compare_java_by_version ${path} version-1.5.0` -ge 0 ] &&
       [ -f ${path}/bin/javaws ]
    then
        path=${path}/bin/javaws
    elif [ `compare_java_by_version ${path} version-1.4.2` -ge 0 ]; then
        if [ -f ${path}/jre/javaws/javaws ]; then
            path=${path}/jre/javaws/javaws
        elif [ -f ${path}/javaws/javaws ]; then
            path=${path}/javaws/javaws
        else
            path=
        fi
    else
        path=
    fi
    echo ${path}
}
    LINK_ERROR_BAD_PARAMS=3000
LINK_ERROR_DEAD_LINK=3001
LINK_ERROR_FILE_NOT_FOUND=3002
dereference() {
    status=0
    if [ "$1" = "-f" ] || [ "$1" = "--follow" ]; then
        follow="--follow"
        shift 1
    fi
    if [ $# -ge 1 ]; then
        path="$*"
        if [ -e "${path}" ]; then
            parent="`cd \`dirname \"${path}\"\`; pwd`"
            child="`basename \"${path}\"`"
            if [ "${parent}" != "${child}" ]; then
                path="${parent}/${child}"
            fi
            if [ -h "${path}" ]; then
                path=`ls -l "${path}" | sed -e "s#^.*${path} -> ##"`
                if [ "`expr substr \"${path}\" 1 1`" != "/" ]; then
                    path="${parent}/${path}"
                fi
                if [ -n "${follow}" ]; then
                    path="`dereference ${follow} ${path}`"
                fi                    
            fi
        else
            status=${LINK_ERROR_FILE_NOT_FOUND}
        fi
    fi
    echo ${path}
    return ${status}
}
setup_latest_link() {
    latest=$1
    link=$2
    if [ -h "${link}" ]; then
        reference="`dereference --follow ${link}`"
        if [ $? -eq 0 ]; then
            update=`compare_java_by_release "${latest}" "${reference}"`
        else
            update=1
        fi
        if [ ${update} -gt 0 ]; then
            rm -f "${link}"
        fi
    fi
    if [ ! -e "${link}" ]; then
        ln -s "${latest}" "${link}"
    fi
}
setup_default_links() {
    if [ $# -ge 2 ]; then
        latest_link="$1"
        default_link="$2"
        if [ ! -e "${default_link}" ]; then
            ln -s "${latest_link}" "${default_link}"
        fi
    fi
    if [ $# -gt 3 ]; then
        bindir="$3"
        shift 3
        for file in $*; do
            reference="`dereference --follow ${bindir}/${file}`"
            if [ $? -ne 0 ]; then
                rm -f "${bindir}/${file}"
            fi
            source="${default_link}/bin/${file}"
            if [ "${file}" = "javaws" ]; then
                source="`get_javaws \"${default_link}\"`"
            fi
            if [ -n "${source}" ] && [ ! -e "${bindir}/${file}" ]; then
                ln -s "${source}" "${bindir}/${file}"
            fi
        done
    fi
}
cleanup_default_links() {
    if [ $# -ge 1 ]; then
        default_link=$1
        if [ $# -gt 2 ]; then
            bindir="$2"
            shift 2
            for file in $*; do
                reference="`dereference \"${bindir}/${file}\"`"
                if [ $? -ne 0 ] ||
                   [ "${reference}" = "${default_link}/bin/${file}" ]
                then
                    rm -f "${bindir}/${file}"
                fi
            done
        fi
        rm -f "${default_link}"
    fi
}


    #
    # Dereference and follow any links that might have been created when this
    # package was installed.  If a link ultimately points to this installation
    # or the link is dead, then we should remove the link.  Important links,
    # like default and latest can be remade in post-uninstall (%postun).
    #
    # This is done in the reverse order the links were initially created in, in
    # case there are any partial loops.
    #
    if [ -h "/usr/java/default" ]; then
        DEFAULT_LINK="`dereference --follow \"/usr/java/default\"`"
        if [ $? -ne 0 ] ||
           [ "${DEFAULT_LINK}" = "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ]
        then
            cleanup_default_links "/usr/java/default" \
                                  "/usr/bin" java javaws jcontrol javac jar javadoc
        fi
    fi

    #
    # If the latest link still points to this installation it must mean one of
    # the following:
    #
    #     * No newer version of Java has been installed.  This is known because
    #       any such version would have already changed the latest to point
    #       to itself.
    #
    #     * No older version is installed.  We don't check this now, but if this
    #       is the case, now is the best time to remove the latest link, since
    #       anything pointing to this installation in post-uninstall will be a
    #       dead link.
    #
    #     * There is an older version of Java installed.  In this case we need
    #       to handle the latest link differently depending on what version
    #       remains.
    #
    if [ -h "/usr/java/latest" ]; then
        LATEST_LINK="`dereference --follow \"/usr/java/latest\"`"
        if [ $? -ne 0 ] ||
           [ "${LATEST_LINK}" = "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ]
        then
            #
            # If this version is the latest, and the first version with jexec
            # support, then stop and remove the jexec service.  If this isn't
            # done now, there might not be an init script left when %postun is
            # called, and if there is, we can restart/reinstall the service
            # easy enough then.
            #
            if [ `compare_java_by_version ${LATEST_LINK} \
                                  version-1.6.0` -ge 0 ] &&
               [ -x /etc/init.d/jexec ]
            then
                /etc/init.d/jexec stop > /dev/null 2>&1

                if [ -x /usr/lib/lsb/remove_initd ]; then
                    /usr/lib/lsb/remove_initd jexec > /dev/null 2>&1
                elif [ -x /sbin/chkconfig ]; then
                    /sbin/chkconfig --del jexec > /dev/null 2>&1
                fi
            fi

            rm -f "/usr/java/latest" 2> /dev/null
        fi
    fi

    #
    # If the package was relocated when it was installed, there should be a link
    # in /usr/java.  So, if there is a link named /usr/java/jdk1.6.0_45 that is
    # dead, or points back to ${RPM_INSTALL_PREFIX}, delete it.
    #
    if [ "${RPM_INSTALL_PREFIX}" != "/usr/java" ] &&
       [ -h "/usr/java/jdk1.6.0_45" ]
    then
        THIS_LINK="`dereference --follow \"/usr/java/jdk1.6.0_45\"`"
        if [ $? -ne 0 ] ||
           [ "${THIS_LINK}" = "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ]
        then
            rm -f "/usr/java/jdk1.6.0_45" 2> /dev/null
        fi
    fi


%postun -p /bin/sh
#
    # Make sure any new files are created with a secure access mask.  Do not use
    # chmod, since that would also change the rights of any existing files, and
    # we are only interested in setting the rights for new files.
    #
    umask 022

    #
    # The package assumes that Gnome is either installed, or going to be
    # installed, so if nothing currently exists, then install in the default
    # location.
    #
    # NOTE: These variables must be defined before all the shell function macros
    #       are included.
    #
    if [ -z "${GNOMEDIR}" ]; then
        GNOMEDIR=/usr
    fi

    #
    # RPM_INSTALL_PREFIX doesn't seem to be set by "alien" so the following
    # minor kludge allows some functionality on debian-like systems (such
    # a Ubuntu) which don't support packages.
    #
    if [ -z "${RPM_INSTALL_PREFIX}" ]; then
	RPM_INSTALL_PREFIX="/usr/java"
    fi

    #
    # Gross kludge for old SuSE distros: Even though they set the environment
    # variable GNOMEDIR to /opt/gnome, Gnome may really be in /opt/gnome2.
    # Go figure,... (I feel so unclean....)
    #
    if [ "${GNOMEDIR}" = "/opt/gnome" ] && [ -d "/opt/gnome2" ]; then
	GNOMEDIR="/opt/gnome2"
    fi

    INSTALL_JRE_PATH=${RPM_INSTALL_PREFIX}/jdk1.6.0_45
    if [ -e ${INSTALL_JRE_PATH}/jre/bin/java ]; then
	INSTALL_JRE_PATH=${INSTALL_JRE_PATH}/jre
    fi

    #
    # Add the shell function and related variables used by the post-uninstall.
    #
    NS_COMMENT1="#--Netscape Communications Corporation MIME Information"
NS_COMMENT2="#Do not delete the above line. It is used to identify the file type."
NS_COMMENT3="#mime types added by Netscape Helper"
UpdateMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    command="$3"
    if [ -z "`grep -E \"^${mime_type}; ${command}$\" \"${mailcap_file}\" 2> /dev/null`" ]; then
        mc_comment="# Java Web Start"
        mc_text=
        if [ -w "${mailcap_file}" ]; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
        fi
        if [ -w "`dirname \"${mailcap_file}\"`" ]; then
            mc_text="${mc_text:+${mc_text}\n}${mime_type}; ${command}"
            printf "%s" "${mc_text}" > "${mailcap_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mailcap_file}"
            echo "Check permissions."
        fi
    fi
}
RemoveMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    mc_comment="# Java Web Start"
    if [ -w "${mailcap_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mailcap_file}\"`" ] ; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
            if [ `echo "${mc_text}" | tr -d '[:space:]' | wc -c` -gt 0 ]; then
                echo "${mc_text}" > "${mailcap_file}"
            else
                rm -f "${mailcap_file}"
            fi
        fi
    fi
}
UpdateMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    desc="$3"
    shift 3
    exts="$*"
    JNLP_ENTRY="type=${mime_type} desc=\"${desc}\" exts=\"${exts}\""
    if [ ! -w "${mime_file}" ]; then
        if [ -w `dirname ${mime_file}` ]; then
            echo "${NS_COMMENT1}"  > "${mime_file}"
            echo "${NS_COMMENT2}" >> "${mime_file}"
            echo "${NS_COMMENT3}" >> "${mime_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mime_file}"
            echo "Check permissions."
            return
        fi
    fi
    if [ -z "`grep -E \"^[^#]*${mime_type}\" \"${mime_file}\"`" ]; then
        echo ${JNLP_ENTRY} >> "${mime_file}"
    fi
}
RemoveMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    if [ -w "${mime_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mime_file}\"`" ]; then
            regexp="(${mime_type})|(^${NS_COMMENT1}$)|(^${NS_COMMENT2}$)|(^${NS_COMMENT3}$)"
            if [ `grep -Ev "${regexp}" "${mime_file}" | \
                 tr -d '[:space:]' | wc -c` -gt 0 ]
            then
                mt_text="`grep -v \"${mime_type}\" \"${mime_file}\"`"
                echo "${mt_text}" > "${mime_file}"
            else
                rm -f "${mime_file}"
            fi
        fi
    fi
}
    MOST_DIGITS="[1-9]"
ALL_DIGITS="[0-9]"
COUNTING_NUMBER="${MOST_DIGITS}${ALL_DIGITS}*\|0"
VALID_NON_NUMERIC="[-_.a-zA-Z]"
VALID_CHARS="[-_.a-zA-Z0-9]"
MAJOR_RULE="\(${MOST_DIGITS}${ALL_DIGITS}*\)"
MINOR_RULE="\(${COUNTING_NUMBER}\)"
MICRO_RULE="\(${COUNTING_NUMBER}\)"
UPDATE_RULE="\(${MOST_DIGITS}${ALL_DIGITS}\|0${ALL_DIGITS}\)"
NON_FCS_ID_RULE="\([a-zA-Z0-9]*\)"
MIN_VERSION_ID_RULE="${MAJOR_RULE}\.${MINOR_RULE}\.${MICRO_RULE}"
FCS_VERSION_ID_RULE="${MIN_VERSION_ID_RULE}\(_${UPDATE_RULE}\)\?"
VERSION_ID_RULE="${FCS_VERSION_ID_RULE}\(-${NON_FCS_ID_RULE}\)\?"
NAME_ID_RULE="${VALID_CHARS}*${VALID_NON_NUMERIC}"
KNOWN_GOOD_NAME_LIST="java jdk jre j2sdk j2re"
PRS_ERROR_BAD_PARAMS=2000
expand_version() {
    status=0
    if [ $# -eq 0 ]; then
        read release remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${release}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${release}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        release=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        \printf "\t expand_version\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        format="%d\t%d\t%d\t%d\n"
        echo ${release} | sed -e "s/_/\./g" | \
          awk -v format="${format}" 'BEGIN { FS = "." } { printf format, $1, $2, $3, $4 }'
    fi
    return ${status}
}
parse_release() {
    status=0
    if [ $# -eq 0 ]; then
        read string remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${string}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${string}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        string=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t parse_release %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        version_id=`expr "${string}" : "${NAME_ID_RULE}\(${VERSION_ID_RULE}\)\$"`
        if [ -n "${version_id}" ]; then
            name_id=`expr "${string}" : "\(${NAME_ID_RULE}\)${VERSION_ID_RULE}\$"`
            fcs_part=`expr "${string}" : "${NAME_ID_RULE}\(${FCS_VERSION_ID_RULE}\).*\$"`
            non_fcs_part=`expr "${version_id}" : "[^-]*-\(${NON_FCS_ID_RULE}\)\$"`
	    printf "%s\t%s\t%s\n" "${name_id}" "${fcs_part}" "${non_fcs_part}"
        fi
    fi
    return ${status}
}
UNKNOWN_NAME_WEIGHT=1000
get_name_weight() {
    status=0
    if [ "$1" = "-" ]; then
        read name good_names
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        else
            shift 1
            if [ $# -gt 0 ]; then
                good_names="$*"
            fi
            if [ -z "${name}" ]; then
                printf "Error: usage - function requires input!\n" >> /dev/stderr
                status=${PRS_ERROR_BAD_PARAMS}
            fi
        fi
    elif [ $# -gt 1 ]; then
        name=$1
        shift 1
        good_names="$*"
    else
        printf "Error: usage - function takes 2+ parameters:\n\n" >> /dev/stderr
        printf "\t get_name_weight %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -n "${good_names}" ]; then
            length=`expr length "${good_names}"`
            pos=`expr "${good_names}" : ".*\<${name}\>"`
            if [ ${pos} -gt 0 ]; then
                expr substr "${good_names}" 1 ${pos} | wc -w | tr -d "[:space:]"
            else
                echo ${UNKNOWN_NAME_WEIGHT}
            fi
        else
            echo ${UNKNOWN_NAME_WEIGHT}
        fi
    fi
    return ${status}
}
HAS_FCS_WEIGHT=0
HAS_ODD_FCS_WEIGHT=1
HAS_RC_WEIGHT=100
HAS_ODD_RC_WEIGHT=101
HAS_BETA_WEIGHT=300
HAS_ODD_BETA_WEIGHT=301
HAS_EA_WEIGHT=500
HAS_ODD_EA_WEIGHT=501
HAS_INTRNAL_WEIGHT=2000
HAS_VERY_ODD_WEIGHT=9999
get_non_fcs_weight() {
    status=0
    if [ $# -eq 0 ]; then
        read non_fcs_part remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${non_fcs_part}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        non_fcs_part=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t get_non_fcs_weight \n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -z "${non_fcs_part}" ]; then
            echo ${HAS_FCS_WEIGHT}
        else
            case "${non_fcs_part}" in
                fcs)
                    echo ${HAS_ODD_FCS_WEIGHT}
                    ;;
                rc)
                    echo ${HAS_RC_WEIGHT}
                    ;;
                rc[0-9] | rc[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "rc\([0-9]*\)$"`
                    echo `expr ${HAS_RC_WEIGHT} - ${count}`
                    ;;
                rc*)
                    echo ${HAS_ODD_RC_WEIGHT}
                    ;;
                beta)
                    echo ${HAS_BETA_WEIGHT}
                    ;;
                beta[0-9] | beta[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "beta\([0-9]*\)$"`
                    echo `expr ${HAS_BETA_WEIGHT} - ${count}`
                    ;;
                beta*)
                    echo ${HAS_ODD_BETA_WEIGHT}
                    ;;
                ea)
                    echo ${HAS_EA_WEIGHT}
                    ;;
                ea[0-9] | ea[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "ea\([0-9]*\)$"`
                    echo `expr ${HAS_EA_WEIGHT} - ${count}`
                    ;;
                ea*)
                    echo ${HAS_ODD_EA_WEIGHT}
                    ;;
                internal)
                    echo ${HAS_INTRNAL_WEIGHT}
                    ;;
                internal[0-9] | internal[0-9][0-9] | internal[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "internal\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                b[0-9] | b[0-9][0-9] | b[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "b\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                *)
                    echo ${HAS_VERY_ODD_WEIGHT}
                    ;;
            esac
        fi
    fi
    return ${status}
}
    get_path_weight() {
    good_list="$1"
    path=$2
    release=`basename ${path}`
    parts="`parse_release ${release}`"
    if [ $? -eq 0 ]; then
        name=`echo "${parts}" | cut -f1`
        version=`echo "${parts}" | cut -f2`
        non_fcs=`echo "${parts}" | cut -f3`
        if [ -n "${version}" ]; then
           v_weight=`echo ${version} | expand_version`
           n_weight=`echo ${name} | get_name_weight - "${good_list}"`
           o_weight=`echo ${non_fcs} | get_non_fcs_weight`
           printf "%4d  %4d  %4d  %4d  %4d  %4d  %s\n" \
                  ${v_weight} ${n_weight} ${o_weight} "${path}"
        fi
    fi
}
get_weighted_list() {
    good_list=
    verify=
    stdio=
    status=0
    check=true
    while [ -n "${check}" ]; do
        if [ $# -gt 0 ]; then
            case "$1" in
                -g)
                    good_list="$2"
                    shift 2
                    ;;
                --good-list=*)
                    length=`expr length "$1"`
                    remove=`expr \( length "--good-list=" \) + 1`
                    good_list="`expr substr \"$1\" ${remove} ${length}`"
                    shift 1
                    ;;
                -v | --verify)
                    verify=true
                    shift 1
                    ;;
                --)
                    shift 1
                    check=
                    ;;
                -)
                    shift 1
                    stdio=true
                    ;;
                -*)
                    printf "Error: usage - unknown parameter:\n\n" \
								>> /dev/stderr
                    printf "\t%s : %s\n" "$1" "$*"		>> /dev/stderr
                    status=${PRS_ERROR_BAD_PARAMS}
                    check=
                    ;;
                *)
                    check=
                    ;;
            esac
        else
            check=
        fi
    done
    if [ $# -eq 0 ] || [ -n "${stdio}" ]; then
        read line
        while [ -n "${line}" ]; do
            if [ -z "${verify}" ] || [ -f ${line}/bin/java ]; then
                get_path_weight "${good_list}" ${line}
            fi
            read line
        done
    fi
    while [ $# -gt 0 ]; do
        if [ -z "${verify}" ] || [ -f $1/bin/java ]; then
            get_path_weight "${good_list}" $1
        fi
        shift 1
    done
    return ${status}
}
_compare_java_by_weight() {
    compare=0
    if [ $# -ne 0 ]; then
        if [ $# -eq 1 ]; then
            compare=1
        else
            left=$1
            right=$2
            shift 2
            good="$*"
            list=`get_weighted_list --good-list="${good}" \
                    ${left} ${right} | sort -u -k1n -k2n -k3n -k4n -k5rn -k6rn`
            if [ `echo "${list}" | wc -l | tr -d "[:space:]"` -ne 1 ]; then
                compare=-1
                latest=`echo "${list}" | tail -n 1 | cut -c 37-`
                if [ "${left}" = "${latest}" ]; then
                    compare=1
                fi
            fi
        fi
    fi
    echo ${compare}
}
compare_java_by_version() {
    _compare_java_by_weight $1 $2
}
compare_java_by_release() {
    _compare_java_by_weight $1 $2 ${KNOWN_GOOD_NAME_LIST}
}
find_latest_release() {
    if [ -d /usr/java ]; then
        latest_release=`find /usr/java/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
    fi
    if [ -d "${RPM_INSTALL_PREFIX}" ] && \
       [ "/usr/java" != "${RPM_INSTALL_PREFIX}" ]
    then 
        prefix_release=`find ${RPM_INSTALL_PREFIX}/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
        if [ `compare_java_by_release ${latest_release} ${prefix_release}` -lt 0 ]; then
            latest_release=${prefix_release}
        fi
    fi
    echo ${latest_release}
}
get_javaws() {
    path=$1
    if [ `compare_java_by_version ${path} version-1.5.0` -ge 0 ] &&
       [ -f ${path}/bin/javaws ]
    then
        path=${path}/bin/javaws
    elif [ `compare_java_by_version ${path} version-1.4.2` -ge 0 ]; then
        if [ -f ${path}/jre/javaws/javaws ]; then
            path=${path}/jre/javaws/javaws
        elif [ -f ${path}/javaws/javaws ]; then
            path=${path}/javaws/javaws
        else
            path=
        fi
    else
        path=
    fi
    echo ${path}
}
    LINK_ERROR_BAD_PARAMS=3000
LINK_ERROR_DEAD_LINK=3001
LINK_ERROR_FILE_NOT_FOUND=3002
dereference() {
    status=0
    if [ "$1" = "-f" ] || [ "$1" = "--follow" ]; then
        follow="--follow"
        shift 1
    fi
    if [ $# -ge 1 ]; then
        path="$*"
        if [ -e "${path}" ]; then
            parent="`cd \`dirname \"${path}\"\`; pwd`"
            child="`basename \"${path}\"`"
            if [ "${parent}" != "${child}" ]; then
                path="${parent}/${child}"
            fi
            if [ -h "${path}" ]; then
                path=`ls -l "${path}" | sed -e "s#^.*${path} -> ##"`
                if [ "`expr substr \"${path}\" 1 1`" != "/" ]; then
                    path="${parent}/${path}"
                fi
                if [ -n "${follow}" ]; then
                    path="`dereference ${follow} ${path}`"
                fi                    
            fi
        else
            status=${LINK_ERROR_FILE_NOT_FOUND}
        fi
    fi
    echo ${path}
    return ${status}
}
setup_latest_link() {
    latest=$1
    link=$2
    if [ -h "${link}" ]; then
        reference="`dereference --follow ${link}`"
        if [ $? -eq 0 ]; then
            update=`compare_java_by_release "${latest}" "${reference}"`
        else
            update=1
        fi
        if [ ${update} -gt 0 ]; then
            rm -f "${link}"
        fi
    fi
    if [ ! -e "${link}" ]; then
        ln -s "${latest}" "${link}"
    fi
}
setup_default_links() {
    if [ $# -ge 2 ]; then
        latest_link="$1"
        default_link="$2"
        if [ ! -e "${default_link}" ]; then
            ln -s "${latest_link}" "${default_link}"
        fi
    fi
    if [ $# -gt 3 ]; then
        bindir="$3"
        shift 3
        for file in $*; do
            reference="`dereference --follow ${bindir}/${file}`"
            if [ $? -ne 0 ]; then
                rm -f "${bindir}/${file}"
            fi
            source="${default_link}/bin/${file}"
            if [ "${file}" = "javaws" ]; then
                source="`get_javaws \"${default_link}\"`"
            fi
            if [ -n "${source}" ] && [ ! -e "${bindir}/${file}" ]; then
                ln -s "${source}" "${bindir}/${file}"
            fi
        done
    fi
}
cleanup_default_links() {
    if [ $# -ge 1 ]; then
        default_link=$1
        if [ $# -gt 2 ]; then
            bindir="$2"
            shift 2
            for file in $*; do
                reference="`dereference \"${bindir}/${file}\"`"
                if [ $? -ne 0 ] ||
                   [ "${reference}" = "${default_link}/bin/${file}" ]
                then
                    rm -f "${bindir}/${file}"
                fi
            done
        fi
        rm -f "${default_link}"
    fi
}

    #
    # The RPM update command installs a given version of a package, and then
    # uninstalls all other versions of a package.
    #
    # The command does the following:
    #
    #     1) Run the %pre for the package being installed
    #     2) Install the new package's files
    #     3) Run the %post for the package being installed
    #     4) Run the %preun for each package being uninstalled
    #     5) Delete any old files not overwitten by the package being installed
    #     6) Run the %postun for each package being uninstalled
    #
    # Note: Because each version of Java installs into its own unique directory,
    #       the only files in step 5 that might not be deleted are the files in
    #       /etc/.java/.systemPrefs that are used for the Preferences API.
    #
    # Note: The order described above is also the same order that occurs when a
    #       user installs a new version, then uninstalls an old version at a
    #       later date.  The only difference is the ammount of time that passes
    #       between steps 3 and 4.
    #
    # Because of this order, all changes made to the system by the package
    # being installed are made *before* any changes made by packages being
    # uninstalled. This means that it is important that the %preun and %postun
    # scriptlets are written in a way that does not break any integration just
    # setup by the new package.  This makes it very difficult to determine what
    # should and shouldn't be removed during %preun and %postun scriptlets.
    #
    # Packages written in the past have no idea what the future will hold.  This
    # is obvious, but it doesn't make it easy.  One option is to assume users
    # will always install newer versions over older versions, and will never
    # keep multiple versions of the same package installed at the same time.
    # This is actually the assumption that RPM is designed upon.
    #
    # However, the --force option can be used to force RPM to install an older
    # package; a so called downgrade.  In the past, Java RPM packages have
    # always attempted to provide special support for downgrades.  This can
    # cause a lot of trouble given the design of RPM.
    #
    # This spec follows the recomended RPM practice.  If the version being
    # uninstalled is not the latest version, then nothing is done.  However, if
    # the version being uninstalled is the latest, then anything setup by the
    # %post scriptlet that is not also tracked by the RPM database is removed.
    #
    # Unfortunately there are two damned kinds of Java installations for every
    # given release, i.e. a JDK and a JRE.  Because of this, it is possible that
    # this version being uninstalled is the latest version, and that the version
    # being left behind is the *same* version as this!
    #
    # In this case, it is necessary to fix anything just broken by the %preun
    # scriptlet.  This will only happen when the JDK is uninstalled, and the
    # JRE of the same version is still on the system.  For this, all that needs
    # to be done is to repair the default and latest links.

    #
    # Determine if a new latest link should be created.  This is done if
    # there is still an installed version of Java that is 1.6 up to the
    # the version of this package.
    #
    LATEST_JAVA_PATH="`find_latest_release`"
    if [ -n "${LATEST_JAVA_PATH}" ] &&
       [ `compare_java_by_version ${LATEST_JAVA_PATH} \
                                  version-1.6.0_45` -lt 0 ]
    then
        #
        # Only maintain the latest link if the latest version left on
        # the system is the ugly stepsister to this one, i.e. this is
	# the JDK, and the JRE of the same version remains.
        #
        # Note: if the latest is higher than the version of this
        #       package, then latest will either A) already exist,
        #       so there is nothing that needs to be done, or B) the
        #       latest link is no longer supported buy those versions,
        #       so this package shouldn't set it up.
        #
        setup_latest_link "${LATEST_JAVA_PATH}" "/usr/java/latest"
    fi


    if [ -n "${LATEST_JAVA_PATH}" ]; then
        #
        # We just removed the Prefernce API files, so restore them since there
        # is still a version of Java installed.
        #
        mkdir -p /etc/.java/.systemPrefs
        if [ -f /etc/.java/.systemPrefs/.system.lock.rpmsave ]; then
            mv /etc/.java/.systemPrefs/.system.lock.rpmsave \
               /etc/.java/.systemPrefs/.system.lock
        elif [ ! -f /etc/.java/.systemPrefs/.system.lock ]; then
            touch /etc/.java/.systemPrefs/.system.lock
        fi
        if [ -f /etc/.java/.systemPrefs/.systemRootModFile.rpmsave ]; then
            mv /etc/.java/.systemPrefs/.systemRootModFile.rpmsave \
               /etc/.java/.systemPrefs/.systemRootModFile
        elif [ ! -f /etc/.java/.systemPrefs/.systemRootModFile ]; then
            touch /etc/.java/.systemPrefs/.systemRootModFile
        fi
    fi

    if [ -e "/usr/java/latest" ]; then
        #
        # If the latest link exists, then make sure the default link exists.
        #
        # Note: instead of trying to determine whether or not the current latest
        #       installation is a JDK or a JRE, just assume it's a JDK.
        #
        setup_default_links "/usr/java/latest" "/usr/java/default" \
                            "/usr/bin" "java javaws jcontrol javac jar javadoc"

        #
        # If there is still an init script kicking around then restart/reinstall
        # it in case it was stopped/uninstalled during %preun.
        #
        if [ -x /etc/init.d/jexec ]; then
            #
            # Try to register the init script to the various run levels.  If
            # possible this is accomplished using an LSB defined install tool.
            # If that isn't available, then try to use chkconfig, which is
            # supported by Red Hat and Debian.  Otherwise it is up to the user
            # to get the script setup for their distribution.
            #
            if [ -x /usr/lib/lsb/install_initd ]; then
                /usr/lib/lsb/install_initd jexec > /dev/null 2>&1

                # start the service for the current session
                /etc/init.d/jexec start > /dev/null 2>&1
            elif [ -x /sbin/chkconfig ]; then
                /sbin/chkconfig --add jexec > /dev/null 2>&1

                # start the service for the current session
                /etc/init.d/jexec start > /dev/null 2>&1
            fi
        fi
    fi






%verifyscript -p /bin/sh
#
    # Make sure any new files are created with a secure access mask.  Do not use
    # chmod, since that would also change the rights of any existing files, and
    # we are only interested in setting the rights for new files.
    #
    umask 022

    #
    # The package assumes that Gnome is either installed, or going to be
    # installed, so if nothing currently exists, then install in the default
    # location.
    #
    # NOTE: These variables must be defined before all the shell function macros
    #       are included.
    #
    if [ -z "${GNOMEDIR}" ]; then
        GNOMEDIR=/usr
    fi

    #
    # RPM_INSTALL_PREFIX doesn't seem to be set by "alien" so the following
    # minor kludge allows some functionality on debian-like systems (such
    # a Ubuntu) which don't support packages.
    #
    if [ -z "${RPM_INSTALL_PREFIX}" ]; then
	RPM_INSTALL_PREFIX="/usr/java"
    fi

    #
    # Gross kludge for old SuSE distros: Even though they set the environment
    # variable GNOMEDIR to /opt/gnome, Gnome may really be in /opt/gnome2.
    # Go figure,... (I feel so unclean....)
    #
    if [ "${GNOMEDIR}" = "/opt/gnome" ] && [ -d "/opt/gnome2" ]; then
	GNOMEDIR="/opt/gnome2"
    fi

    INSTALL_JRE_PATH=${RPM_INSTALL_PREFIX}/jdk1.6.0_45
    if [ -e ${INSTALL_JRE_PATH}/jre/bin/java ]; then
	INSTALL_JRE_PATH=${INSTALL_JRE_PATH}/jre
    fi
    #
    # Add the shell function and related variables used by the verify script.
    #
    NS_COMMENT1="#--Netscape Communications Corporation MIME Information"
NS_COMMENT2="#Do not delete the above line. It is used to identify the file type."
NS_COMMENT3="#mime types added by Netscape Helper"
UpdateMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    command="$3"
    if [ -z "`grep -E \"^${mime_type}; ${command}$\" \"${mailcap_file}\" 2> /dev/null`" ]; then
        mc_comment="# Java Web Start"
        mc_text=
        if [ -w "${mailcap_file}" ]; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
        fi
        if [ -w "`dirname \"${mailcap_file}\"`" ]; then
            mc_text="${mc_text:+${mc_text}\n}${mime_type}; ${command}"
            printf "%s" "${mc_text}" > "${mailcap_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mailcap_file}"
            echo "Check permissions."
        fi
    fi
}
RemoveMailcap() {
    mailcap_file="$1"
    mime_type="$2"
    mc_comment="# Java Web Start"
    if [ -w "${mailcap_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mailcap_file}\"`" ] ; then
            regexp="(${mime_type})|(${mc_comment})"
            mc_text=`grep -Ev "${regexp}" "${mailcap_file}"`
            if [ `echo "${mc_text}" | tr -d '[:space:]' | wc -c` -gt 0 ]; then
                echo "${mc_text}" > "${mailcap_file}"
            else
                rm -f "${mailcap_file}"
            fi
        fi
    fi
}
UpdateMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    desc="$3"
    shift 3
    exts="$*"
    JNLP_ENTRY="type=${mime_type} desc=\"${desc}\" exts=\"${exts}\""
    if [ ! -w "${mime_file}" ]; then
        if [ -w `dirname ${mime_file}` ]; then
            echo "${NS_COMMENT1}"  > "${mime_file}"
            echo "${NS_COMMENT2}" >> "${mime_file}"
            echo "${NS_COMMENT3}" >> "${mime_file}"
        else
            echo "WARNING - cannot write to file:"
            echo "       ${mime_file}"
            echo "Check permissions."
            return
        fi
    fi
    if [ -z "`grep -E \"^[^#]*${mime_type}\" \"${mime_file}\"`" ]; then
        echo ${JNLP_ENTRY} >> "${mime_file}"
    fi
}
RemoveMimeTypes() {
    mime_file="$1"
    mime_type="$2"
    if [ -w "${mime_file}" ]; then
        if [ -n "`grep \"${mime_type}\" \"${mime_file}\"`" ]; then
            regexp="(${mime_type})|(^${NS_COMMENT1}$)|(^${NS_COMMENT2}$)|(^${NS_COMMENT3}$)"
            if [ `grep -Ev "${regexp}" "${mime_file}" | \
                 tr -d '[:space:]' | wc -c` -gt 0 ]
            then
                mt_text="`grep -v \"${mime_type}\" \"${mime_file}\"`"
                echo "${mt_text}" > "${mime_file}"
            else
                rm -f "${mime_file}"
            fi
        fi
    fi
}
    MOST_DIGITS="[1-9]"
ALL_DIGITS="[0-9]"
COUNTING_NUMBER="${MOST_DIGITS}${ALL_DIGITS}*\|0"
VALID_NON_NUMERIC="[-_.a-zA-Z]"
VALID_CHARS="[-_.a-zA-Z0-9]"
MAJOR_RULE="\(${MOST_DIGITS}${ALL_DIGITS}*\)"
MINOR_RULE="\(${COUNTING_NUMBER}\)"
MICRO_RULE="\(${COUNTING_NUMBER}\)"
UPDATE_RULE="\(${MOST_DIGITS}${ALL_DIGITS}\|0${ALL_DIGITS}\)"
NON_FCS_ID_RULE="\([a-zA-Z0-9]*\)"
MIN_VERSION_ID_RULE="${MAJOR_RULE}\.${MINOR_RULE}\.${MICRO_RULE}"
FCS_VERSION_ID_RULE="${MIN_VERSION_ID_RULE}\(_${UPDATE_RULE}\)\?"
VERSION_ID_RULE="${FCS_VERSION_ID_RULE}\(-${NON_FCS_ID_RULE}\)\?"
NAME_ID_RULE="${VALID_CHARS}*${VALID_NON_NUMERIC}"
KNOWN_GOOD_NAME_LIST="java jdk jre j2sdk j2re"
PRS_ERROR_BAD_PARAMS=2000
expand_version() {
    status=0
    if [ $# -eq 0 ]; then
        read release remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${release}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${release}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        release=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        \printf "\t expand_version\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        format="%d\t%d\t%d\t%d\n"
        echo ${release} | sed -e "s/_/\./g" | \
          awk -v format="${format}" 'BEGIN { FS = "." } { printf format, $1, $2, $3, $4 }'
    fi
    return ${status}
}
parse_release() {
    status=0
    if [ $# -eq 0 ]; then
        read string remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -z "${string}" ]; then
            printf "Error: usage - function requires input!\n"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${string}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        string=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t parse_release %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        version_id=`expr "${string}" : "${NAME_ID_RULE}\(${VERSION_ID_RULE}\)\$"`
        if [ -n "${version_id}" ]; then
            name_id=`expr "${string}" : "\(${NAME_ID_RULE}\)${VERSION_ID_RULE}\$"`
            fcs_part=`expr "${string}" : "${NAME_ID_RULE}\(${FCS_VERSION_ID_RULE}\).*\$"`
            non_fcs_part=`expr "${version_id}" : "[^-]*-\(${NON_FCS_ID_RULE}\)\$"`
	    printf "%s\t%s\t%s\n" "${name_id}" "${fcs_part}" "${non_fcs_part}"
        fi
    fi
    return ${status}
}
UNKNOWN_NAME_WEIGHT=1000
get_name_weight() {
    status=0
    if [ "$1" = "-" ]; then
        read name good_names
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        else
            shift 1
            if [ $# -gt 0 ]; then
                good_names="$*"
            fi
            if [ -z "${name}" ]; then
                printf "Error: usage - function requires input!\n" >> /dev/stderr
                status=${PRS_ERROR_BAD_PARAMS}
            fi
        fi
    elif [ $# -gt 1 ]; then
        name=$1
        shift 1
        good_names="$*"
    else
        printf "Error: usage - function takes 2+ parameters:\n\n" >> /dev/stderr
        printf "\t get_name_weight %s\n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -n "${good_names}" ]; then
            length=`expr length "${good_names}"`
            pos=`expr "${good_names}" : ".*\<${name}\>"`
            if [ ${pos} -gt 0 ]; then
                expr substr "${good_names}" 1 ${pos} | wc -w | tr -d "[:space:]"
            else
                echo ${UNKNOWN_NAME_WEIGHT}
            fi
        else
            echo ${UNKNOWN_NAME_WEIGHT}
        fi
    fi
    return ${status}
}
HAS_FCS_WEIGHT=0
HAS_ODD_FCS_WEIGHT=1
HAS_RC_WEIGHT=100
HAS_ODD_RC_WEIGHT=101
HAS_BETA_WEIGHT=300
HAS_ODD_BETA_WEIGHT=301
HAS_EA_WEIGHT=500
HAS_ODD_EA_WEIGHT=501
HAS_INTRNAL_WEIGHT=2000
HAS_VERY_ODD_WEIGHT=9999
get_non_fcs_weight() {
    status=0
    if [ $# -eq 0 ]; then
        read non_fcs_part remainder
        status=$?
        if [ ${status} -ne 0 ]; then
            printf "Error(%s): failed to read!\n" "${status}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        elif [ -n "${remainder}" ]; then
            printf "Error: too many words read:\n\n"		>> /dev/stderr
            printf "\t%s %s\n" "${non_fcs_part}" "${remainder}"	>> /dev/stderr
            status=${PRS_ERROR_BAD_PARAMS}
        fi
    elif [ $# -eq 1 ]; then
        non_fcs_part=$1
    else
        printf "Error: usage - function takes 1 parameter:\n\n"	>> /dev/stderr
        printf "\t get_non_fcs_weight \n" "$*"			>> /dev/stderr
        status=${PRS_ERROR_BAD_PARAMS}
    fi
    if [ ${status} -eq 0 ]; then
        if [ -z "${non_fcs_part}" ]; then
            echo ${HAS_FCS_WEIGHT}
        else
            case "${non_fcs_part}" in
                fcs)
                    echo ${HAS_ODD_FCS_WEIGHT}
                    ;;
                rc)
                    echo ${HAS_RC_WEIGHT}
                    ;;
                rc[0-9] | rc[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "rc\([0-9]*\)$"`
                    echo `expr ${HAS_RC_WEIGHT} - ${count}`
                    ;;
                rc*)
                    echo ${HAS_ODD_RC_WEIGHT}
                    ;;
                beta)
                    echo ${HAS_BETA_WEIGHT}
                    ;;
                beta[0-9] | beta[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "beta\([0-9]*\)$"`
                    echo `expr ${HAS_BETA_WEIGHT} - ${count}`
                    ;;
                beta*)
                    echo ${HAS_ODD_BETA_WEIGHT}
                    ;;
                ea)
                    echo ${HAS_EA_WEIGHT}
                    ;;
                ea[0-9] | ea[0-9][0-9])
                    count=`expr "${non_fcs_part}" : "ea\([0-9]*\)$"`
                    echo `expr ${HAS_EA_WEIGHT} - ${count}`
                    ;;
                ea*)
                    echo ${HAS_ODD_EA_WEIGHT}
                    ;;
                internal)
                    echo ${HAS_INTRNAL_WEIGHT}
                    ;;
                internal[0-9] | internal[0-9][0-9] | internal[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "internal\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                b[0-9] | b[0-9][0-9] | b[0-9][0-9][0-9])
                    count=`expr "${non_fcs_part}" : "b\([0-9]*\)$"`
                    echo `expr ${HAS_INTRNAL_WEIGHT} - ${count}`
                    ;;
                *)
                    echo ${HAS_VERY_ODD_WEIGHT}
                    ;;
            esac
        fi
    fi
    return ${status}
}
    get_path_weight() {
    good_list="$1"
    path=$2
    release=`basename ${path}`
    parts="`parse_release ${release}`"
    if [ $? -eq 0 ]; then
        name=`echo "${parts}" | cut -f1`
        version=`echo "${parts}" | cut -f2`
        non_fcs=`echo "${parts}" | cut -f3`
        if [ -n "${version}" ]; then
           v_weight=`echo ${version} | expand_version`
           n_weight=`echo ${name} | get_name_weight - "${good_list}"`
           o_weight=`echo ${non_fcs} | get_non_fcs_weight`
           printf "%4d  %4d  %4d  %4d  %4d  %4d  %s\n" \
                  ${v_weight} ${n_weight} ${o_weight} "${path}"
        fi
    fi
}
get_weighted_list() {
    good_list=
    verify=
    stdio=
    status=0
    check=true
    while [ -n "${check}" ]; do
        if [ $# -gt 0 ]; then
            case "$1" in
                -g)
                    good_list="$2"
                    shift 2
                    ;;
                --good-list=*)
                    length=`expr length "$1"`
                    remove=`expr \( length "--good-list=" \) + 1`
                    good_list="`expr substr \"$1\" ${remove} ${length}`"
                    shift 1
                    ;;
                -v | --verify)
                    verify=true
                    shift 1
                    ;;
                --)
                    shift 1
                    check=
                    ;;
                -)
                    shift 1
                    stdio=true
                    ;;
                -*)
                    printf "Error: usage - unknown parameter:\n\n" \
								>> /dev/stderr
                    printf "\t%s : %s\n" "$1" "$*"		>> /dev/stderr
                    status=${PRS_ERROR_BAD_PARAMS}
                    check=
                    ;;
                *)
                    check=
                    ;;
            esac
        else
            check=
        fi
    done
    if [ $# -eq 0 ] || [ -n "${stdio}" ]; then
        read line
        while [ -n "${line}" ]; do
            if [ -z "${verify}" ] || [ -f ${line}/bin/java ]; then
                get_path_weight "${good_list}" ${line}
            fi
            read line
        done
    fi
    while [ $# -gt 0 ]; do
        if [ -z "${verify}" ] || [ -f $1/bin/java ]; then
            get_path_weight "${good_list}" $1
        fi
        shift 1
    done
    return ${status}
}
_compare_java_by_weight() {
    compare=0
    if [ $# -ne 0 ]; then
        if [ $# -eq 1 ]; then
            compare=1
        else
            left=$1
            right=$2
            shift 2
            good="$*"
            list=`get_weighted_list --good-list="${good}" \
                    ${left} ${right} | sort -u -k1n -k2n -k3n -k4n -k5rn -k6rn`
            if [ `echo "${list}" | wc -l | tr -d "[:space:]"` -ne 1 ]; then
                compare=-1
                latest=`echo "${list}" | tail -n 1 | cut -c 37-`
                if [ "${left}" = "${latest}" ]; then
                    compare=1
                fi
            fi
        fi
    fi
    echo ${compare}
}
compare_java_by_version() {
    _compare_java_by_weight $1 $2
}
compare_java_by_release() {
    _compare_java_by_weight $1 $2 ${KNOWN_GOOD_NAME_LIST}
}
find_latest_release() {
    if [ -d /usr/java ]; then
        latest_release=`find /usr/java/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
    fi
    if [ -d "${RPM_INSTALL_PREFIX}" ] && \
       [ "/usr/java" != "${RPM_INSTALL_PREFIX}" ]
    then 
        prefix_release=`find ${RPM_INSTALL_PREFIX}/* -prune | \
            get_weighted_list -v --good-list="${KNOWN_GOOD_NAME_LIST}" | \
            sort -k1n -k2n -k3n -k4n -k5rn -k6rn | tail -n 1 | cut -c 37-`
        if [ `compare_java_by_release ${latest_release} ${prefix_release}` -lt 0 ]; then
            latest_release=${prefix_release}
        fi
    fi
    echo ${latest_release}
}
get_javaws() {
    path=$1
    if [ `compare_java_by_version ${path} version-1.5.0` -ge 0 ] &&
       [ -f ${path}/bin/javaws ]
    then
        path=${path}/bin/javaws
    elif [ `compare_java_by_version ${path} version-1.4.2` -ge 0 ]; then
        if [ -f ${path}/jre/javaws/javaws ]; then
            path=${path}/jre/javaws/javaws
        elif [ -f ${path}/javaws/javaws ]; then
            path=${path}/javaws/javaws
        else
            path=
        fi
    else
        path=
    fi
    echo ${path}
}
    LINK_ERROR_BAD_PARAMS=3000
LINK_ERROR_DEAD_LINK=3001
LINK_ERROR_FILE_NOT_FOUND=3002
dereference() {
    status=0
    if [ "$1" = "-f" ] || [ "$1" = "--follow" ]; then
        follow="--follow"
        shift 1
    fi
    if [ $# -ge 1 ]; then
        path="$*"
        if [ -e "${path}" ]; then
            parent="`cd \`dirname \"${path}\"\`; pwd`"
            child="`basename \"${path}\"`"
            if [ "${parent}" != "${child}" ]; then
                path="${parent}/${child}"
            fi
            if [ -h "${path}" ]; then
                path=`ls -l "${path}" | sed -e "s#^.*${path} -> ##"`
                if [ "`expr substr \"${path}\" 1 1`" != "/" ]; then
                    path="${parent}/${path}"
                fi
                if [ -n "${follow}" ]; then
                    path="`dereference ${follow} ${path}`"
                fi                    
            fi
        else
            status=${LINK_ERROR_FILE_NOT_FOUND}
        fi
    fi
    echo ${path}
    return ${status}
}
setup_latest_link() {
    latest=$1
    link=$2
    if [ -h "${link}" ]; then
        reference="`dereference --follow ${link}`"
        if [ $? -eq 0 ]; then
            update=`compare_java_by_release "${latest}" "${reference}"`
        else
            update=1
        fi
        if [ ${update} -gt 0 ]; then
            rm -f "${link}"
        fi
    fi
    if [ ! -e "${link}" ]; then
        ln -s "${latest}" "${link}"
    fi
}
setup_default_links() {
    if [ $# -ge 2 ]; then
        latest_link="$1"
        default_link="$2"
        if [ ! -e "${default_link}" ]; then
            ln -s "${latest_link}" "${default_link}"
        fi
    fi
    if [ $# -gt 3 ]; then
        bindir="$3"
        shift 3
        for file in $*; do
            reference="`dereference --follow ${bindir}/${file}`"
            if [ $? -ne 0 ]; then
                rm -f "${bindir}/${file}"
            fi
            source="${default_link}/bin/${file}"
            if [ "${file}" = "javaws" ]; then
                source="`get_javaws \"${default_link}\"`"
            fi
            if [ -n "${source}" ] && [ ! -e "${bindir}/${file}" ]; then
                ln -s "${source}" "${bindir}/${file}"
            fi
        done
    fi
}
cleanup_default_links() {
    if [ $# -ge 1 ]; then
        default_link=$1
        if [ $# -gt 2 ]; then
            bindir="$2"
            shift 2
            for file in $*; do
                reference="`dereference \"${bindir}/${file}\"`"
                if [ $? -ne 0 ] ||
                   [ "${reference}" = "${default_link}/bin/${file}" ]
                then
                    rm -f "${bindir}/${file}"
                fi
            done
        fi
        rm -f "${default_link}"
    fi
}

    #
    # It isn't possible to repair any missing packed JAR files from --verify.
    # This is because the PACK source files are removed during post-install.
    # If an administrator needs to restore missing packed JAR files, they will
    # need to do a --reinstall.
    #

    #
    # If the package was relocated, then temporarily remove the /usr/java
    # link, but only if it really points to this package.
    #
    if [ "${RPM_INSTALL_PREFIX}" != "/usr/java" ] &&
       [ "`dereference --follow \"/usr/java/jdk1.6.0_45\"`" = "${RPM_INSTALL_PREFIX}" ]
    then
        rm -f "/usr/java/jdk1.6.0_45"
    fi

    #
    # Find out what version of Java is the latest.  Don't do any system
    # integration unless this is the latest version.  Otherwise, we make
    # it difficult for future installers.
    #
    LATEST_JAVA_PATH="`find_latest_release`"
    if [ "${LATEST_JAVA_PATH}" == "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" ] ||
       [ "${LATEST_JAVA_PATH}" == "/usr/java/jdk1.6.0_45" ]
    then
        #
        # Make sure the /usr/java/latest link points to LATEST_JAVA_PATH, and
	# update it if it doesn't.
        #
        setup_latest_link "${LATEST_JAVA_PATH}" "/usr/java/latest"

        #
        # Make sure the /usr/java/default and java javaws jcontrol javac jar javadoc exist.
	# If anything is missing, create it.
        #
        setup_default_links "/usr/java/latest" "/usr/java/default" \
                            "/usr/bin" java javaws jcontrol javac jar javadoc

        #
        # If the "latest" link is a JDK, then the latest JRE is a subdir;
	# otherwise it is the same dir.
        #
        DEFAULT_JRE_PATH="/usr/java/default"
        if [ -e "/usr/java/default/jre/bin/java" ]; then
            DEFAULT_JRE_PATH="/usr/java/default/jre"
        fi

	#
    fi

    #
    # If the package is being relocated, then create a link in the default
    # location (/usr/java) to the actual install directory.  Do this
    # last, so it doesn't add unnecessary complexity to the search for the
    # latest release.
    #
    if [ "${RPM_INSTALL_PREFIX}" != "/usr/java" ] &&
       ( [ ! -e "/usr/java/jdk1.6.0_45" ] || [ -h "/usr/java/jdk1.6.0_45" ] )
    then
        rm -f "/usr/java/jdk1.6.0_45"
        ln -s "${RPM_INSTALL_PREFIX}/jdk1.6.0_45" "/usr/java/jdk1.6.0_45"
    fi

    #
    # There should be an init script for jexec on the system.  If it is, then
    # make sure it's installed and running
    #
    if [ -x /etc/init.d/jexec ]; then
        #
        # Try to register the init script to the various run levels.  If
	# possible this is accomplished using an LSB defined install tool.
	# If that isn't available, then try to use chkconfig, which is
	# supported by Red Hat and Debian.  The feature of automatic jar
	# file execution is not support on systems which don't support
	# either of these interfaces.
        #
        if [ -x /usr/lib/lsb/install_initd ]; then
            /usr/lib/lsb/install_initd jexec > /dev/null 2>&1

            # start the service for the current session
            /etc/init.d/jexec start > /dev/null 2>&1
        elif [ -x /sbin/chkconfig ]; then
            /sbin/chkconfig --add jexec > /dev/null 2>&1

            # start the service for the current session
            /etc/init.d/jexec start > /dev/null 2>&1
        fi
    fi




%changelog
* Wed May 01 2013 root - 1.6.0_45-fcs.1
- Specfile created from binary rpm jdk-6u45-linux-amd64.rpm
%endif

# COMMON:

%triggerpostun -- jdk = %{epoch}:%{version}
javadir=/usr/java/jdk%{version}

echo Checking symlinks...
# If we're really uninstalling, then just exit
if [[ $1 -eq 0 ]]; then
    echo Uninstalling... not needed.
    exit 0
fi
if [[ ! -e $javadir ]]; then
    echo $javadir not found... not needed.
    exit 0
fi

# Recreate service tag
if [[ -e $javadir/bin/java ]]; then
    echo Recreating service tag
    $javadir/bin/java com.sun.servicetag.Installer -source "jdk" &> /dev/null
fi

# Recreate symlinks that the preun script removes
if [[ ! -e /usr/java/latest ]]; then
    echo Recreating /usr/java/latest symlink
    ln -s $javadir /usr/java/latest
fi
if [[ ! -e /usr/java/default ]]; then
    echo Recreating /usr/java/default symlink
    ln -s /usr/java/latest /usr/java/default
fi
for prog in jar java javac javadoc javaws jcontrol; do
    if [[ ! -e /usr/bin/$prog ]]; then
        echo Recreating /usr/bin/$prog symlink
        ln -s /usr/java/default/bin/$prog /usr/bin/$prog
    fi
done

# Also turn on jexec
/sbin/chkconfig --add jexec &> /dev/null || :
/etc/init.d/jexec start &> /dev/null || :

