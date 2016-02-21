Summary: OASIS GOC package
Name: oasis-goc
Version: 2.1.0
Release: 1%{?dist} 
Source0: %{name}-%{version}.tar.gz
License: Apache 2.0
Group: Development/Libraries
#BuildRoot requried only on RHEL5
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://www.opensciencegrid.org

%description
This package contains OASIS software for the OSG Global Operations Center

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/share/oasis

(cd share;find *|cpio -pdv $RPM_BUILD_ROOT/usr/share/oasis)
(cd bin;find *|cpio -pdv $RPM_BUILD_ROOT/usr/bin)
find etc|cpio -pdv $RPM_BUILD_ROOT
find var|cpio -pdv $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin
/usr/share/oasis

%package zero
Summary: files for OASIS stratum zero
Group: Development/Libraries
%description zero
This package contains files for oasis.opensciencegrid.org

%files zero
/etc/init.d/oasis-initclean
/etc/httpd/conf.d/oasis.conf
/etc/iptables.d/60-local-oasis
/etc/logrotate.d/oasis
/var/www/html/robots.txt
%defattr(-,root,root)

%package replica
Summary: files for OASIS stratum one
Group: Development/Libraries
%description replica
This package contains files for oasis-replica.opensciencegrid.org

%files replica
/etc/cvmfs/cvmfs_server_hooks.sh
/etc/init.d/oasis-replica-initclean
/etc/httpd/conf.d/cvmfs.conf
/etc/iptables.d/60-local-cvmfs
/etc/logrotate.d/cvmfs
/var/www/html/robots.txt
%defattr(-,root,root)


%package login
Summary: files for OASIS login host
Group: Development/Libraries
%description login
This package contains files for oasis-login.opensciencegrid.org

%files login
/etc/init.d/oasis-login-initclean
/etc/iptables.d/60-local-oasis-login
/etc/sysconfig/gsisshd
%defattr(-,root,root)


%changelog
* Fri Feb 19 2015 Dave Dykstra <dwd@fnal.gov> - 2.1.0-1
- Extracted goc-specific pieces out of oasis package
