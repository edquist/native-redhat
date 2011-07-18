
Name:           vdt-build
Version:        0.0.4
Release:        2%{?dist}
Summary:        Build tools for the VDT

Group:          System Environment/Tools
License:        Apache 2.0
URL:            https://twiki.grid.iu.edu/bin/view/SoftwareTeam/RPMDevelopmentGuide

Source0:        %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%description
%{summary}


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{python_sitelib}/VDTBuildConstants.py*
%{python_sitelib}/VDTBuildUtils.py*
%{python_sitelib}/platform-post.py*
%{python_sitelib}/remote-declare.py*
%{python_sitelib}/remote-task.py*
%doc %{_docdir}/%{name}/sample-vdt-build.ini

%changelog
* Mon Jul 18 2011 Matyas Selmeci <matyas@cs.wisc.edu> 0.0.4-2
- Changed autogenerated mock config to use centos repos until I have a working sl5 mock conf file.

* Mon Jul 18 2011 Matyas Selmeci <matyas@cs.wisc.edu> 0.0.4-1
- Implemented batlab builds
- *.py files moved to python_sitelib. sample ini file moved to /usr/share/doc

* Fri Jul 15 2011 Matyas Selmeci <matyas@cs.wisc.edu> 0.0.3-2
- Fixed SOFTWARE-21

* Fri Jul 15 2011 Matyas Selmeci <matyas@cs.wisc.edu> 0.0.3-1
- Various bugfixes (SOFTWARE-{14,15,16})

* Thu Jul 14 2011 Matyas Selmeci <matyas@cs.wisc.edu> 0.0.2-1
- Python rewrite

* Thu Jul  7 2011 Brian Bockelman <bbockelm@cse.unl.edu> 0.0.1-2
- Made vdt-build obey our own packaging guidelines.

* Fri Jul  1 2011 Brian Bockelman <bbockelm@cse.unl.edu> 0.0.1-1
- Created an initial vdt-build RPM for ease-of-use
- Contains RPM::Toolbox::Spec for now.

