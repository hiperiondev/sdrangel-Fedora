Name:           SoapyHackRF-soapy-hackrf
Version:        0.3.3
Release:        1%{?dist}
Summary:        SoapySDR HackRF module
License:        MIT
Group:          Hardware/Other
URL:            https://github.com/pothosware/SoapyHackRF/wiki
#Git-Clone:     https://github.com/pothosware/SoapyHackRF.git
Source:         https://github.com/pothosware/SoapyHackRF/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  hackrf-devel

%description
Soapy HackRF - HackRF device support for Soapy SDR.
A Soapy module that supports HackRF devices within the Soapy API.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules0.7
%{_libdir}/SoapySDR/modules0.7/libHackRFSupport.so

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec

