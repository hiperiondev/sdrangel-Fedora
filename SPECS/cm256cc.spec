Name:           cm256cc
Version:        1.0.5
Release:        1%{?dist}
Summary:        Fast GF(256) Cauchy MDS Block Erasure Codec in C++
License:        BSD-2-Clause
Group:          Development/Languages/C and C++
URL:            https://github.com/f4exb/cm256cc
Source:         https://github.com/f4exb/cm256cc/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
This is the rewrite in (as much as possible) clean C++ of cm256.
cm256cc is a simple library for erasure codes. From given data it
generates redundant data that can be used to recover the originals.

%package devel
Summary:        Development files for the cm256cc library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This is the rewrite in (as much as possible) clean C++ of cm256.
cm256cc is a simple library for erasure codes. From given data it
generates redundant data that can be used to recover the originals.

This subpackage contains libraries and header files for developing
applications that want to make use of libcm256cc.

%prep
%autosetup

%build
%cmake
%make_build

%install
%cmake_install

%files
%doc README.md
%{_bindir}/cm256_rx
%{_bindir}/cm256_test
%{_bindir}/cm256_tx
%{_libdir}/libcm256cc.so.1*

%files devel
%{_includedir}/cm256cc
%{_libdir}/libcm256cc.so
%{_libdir}/pkgconfig/libcm256cc.pc

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec
