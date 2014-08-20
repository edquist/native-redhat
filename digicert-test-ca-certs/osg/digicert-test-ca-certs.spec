Name:           digicert-test-ca-certs
Version:        1.0
Release:        4%{?dist}
Summary:        OSG Packaging of the Digicert test CA Certs, in new OpenSSL 0.9.8/1.0.0 format

Group:          System Environment/Base
License:        Unknown
URL:            http://www.digicert-grid.com/

Source0:        digicert-test-ca.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
%{summary}

%prep
%setup -q -n digicert-test-ca

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/grid-security/certificates
chmod 0644 *
mv * $RPM_BUILD_ROOT/etc/grid-security/certificates/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,-)
%dir %attr(0755,root,root) /etc/grid-security/certificates
/etc/grid-security/certificates/*
%doc

%changelog
* Thu Nov 28 2011 Anand Padmanabhan <apadmana@uiuc.edu> - 1.0-4
- use mv instead of install to maintain symlink

* Mon Nov 14 2011 Anand Padmanabhan <apadmana@uiuc.edu> - 1.0-1
- Initial packaging of the Digicert Test CA certs (new format) from OSG.
