
Name:      rsv
Summary:   RSV Meta Package
Version:   3.4.3
Release:   1
License:   Apache 2.0
Group:     Applications/Monitoring
URL:       https://twiki.grid.iu.edu/bin/view/MonitoringInformation/RSV
BuildArch: noarch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires: rsv-consumers
Requires: rsv-core
Requires: rsv-metrics

%description
%{summary}

%install
# No files to install or directories to make

%clean
rm -rf $RPM_BUILD_ROOT

%files
# No files since this is a meta package

%changelog
* Thu Jul 20 2011 Scot Kronenfeld <kronenfe@cs.wisc.edu> 3.4.0
- Created an initial RSV meta package

