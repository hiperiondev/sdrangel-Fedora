Name:           serialDV
Version:        1.1.4
Release:        1%{?dist}
Summary:        Library for audio de-/encoding with ABME3000 based devices
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/f4exb/serialDV
#Git-Clone:     https://github.com/f4exb/serialDV.git
Source:         https://github.com/f4exb/serialDV/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A library that provides an interface for audio encoding and decoding with
AMBE3000 based devices in packet mode over a serial link.

%package devel
Summary:        Development files for libserialdv
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
A library that provides an interface for audio encoding and decoding with
AMBE3000 based devices in packet mode over a serial link.

This subpackage contains libraries and header files for developing
applications that want to make use of libserialdv.

%package doc
Summary:        Documentation for AMBE3000 based devices

%description doc
Documentation for AMBE3000 based devices

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libserialdv.so*

%files devel
%{_bindir}/dvtest
%{_includedir}/serialdv/
%{_libdir}/libserialdv.so

%files doc
%doc Readme.md

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com - 1.1.4-1
- First Fedora spec

