Name:      osg-gridftp
Summary:   Standalone OSG GridFTP w/lcmaps gums client
Version:   3.0.0
Release:   3
License:   Apache 2.0
Group:     Grid
URL:       http://www.opensciencegrid.org
BuildArch: noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: globus-gridftp-server-progs
Requires: vo-client
Requires: grid-certificates
Requires: gratia-probe-gridftp-transfer
Requires: gums-client

%ifarch %{ix86}
Requires: liblcas_lcmaps_gt4_mapping.so.0()(32bit)
%else
Requires: liblcas_lcmaps_gt4_mapping.so.0()(64bit)
%endif

# This should also pull in lcas, lcmaps, and various plugins
# (basic, proxy verify, posix, etc)

%description
This is a meta package for a standalone GridFTP server with 
gums support through lcmaps plugin and vo-client.

%build

%install

%clean
rm -rf $RPM_BUILD_ROOT

%files


%changelog
* Fri Aug 26 2011 Doug Strain <dstrain.fnal.gov> 
- Created an initial gridftp-standalone meta package RPM.

