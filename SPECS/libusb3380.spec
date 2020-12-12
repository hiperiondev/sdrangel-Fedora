%global commit c83d1e93eb3a5b8b6a9db41c2613b206f344f825
%global short %(c=%{commit}; echo ${c:0:10})
%global date 20190125
Name:           libusb3380
Version:        0
Release:        0.%{date}git%{short}%{?dist}
Summary:        USB3380 abstraction layer for libusb
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://xtrx.io
#Git-Clone:     https://github.com/xtrx-sdr/libusb3380.git
Source:         https://github.com/xtrx-sdr/libusb3380.git/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)

%description
USB3380 abstraction layer for libusb.

%package devel
Summary:        Development files for libusb3380
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
USB3380 abstraction layer for libusb.

This subpackage contains libraries and header files for developing
applications that want to make use of libusb3380.

%prep
%setup -q
#%patch0 -p1

%build
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS=""
%make_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libusb3380.so*

%files devel
%{_includedir}/libusb3380.h
%{_libdir}/libusb3380.so
%{_libdir}/pkgconfig/libusb3380.pc

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec
