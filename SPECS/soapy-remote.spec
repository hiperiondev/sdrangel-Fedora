Name:           SoapyRemote-soapy-remote
Version:        0.5.2
Release:        1%{?dist}
Summary:        Remote device support for Soapy SDR
License:        BSL-1.0
Group:          Productivity/Hamradio/Other
URL:            https://github.com/pothosware/SoapyRemote 
#Git-Clone:     https://github.com/pothosware/SoapyRemote.git
Source:         https://github.com/pothosware/SoapyRemote/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(SoapySDR)

%description
A Soapy module that supports remote devices within the Soapy API.

%package doc
Summary:        Documentation for SoapyRemote

%description doc
Documentation for SoapyRemote

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
# FIXME: should be handled - disabled for now
rm %{buildroot}//usr/lib/sysctl.d/SoapySDRServer.conf
rm %{buildroot}//usr/lib/systemd/system/SoapySDRServer.service

%files
%license LICENSE_1_0.txt
%{_bindir}/SoapySDRServer
%{_mandir}/man1/SoapySDRServer.1.gz
%dir %{_libdir}/SoapySDR/
%dir %{_libdir}/SoapySDR/modules0.7
%{_libdir}/SoapySDR/modules0.7/libremoteSupport.so

%files doc
%doc Changelog.txt README.md

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com - 0.5.2-1
- First Fedora spec
