Name:		mbelib
Version:	1.3.0
Release:	1%{?dist}
Summary:	P25 Phase 1 and ProVoice vocoder
Group:		Applications/Engineering
License:	ISC
URL:            https://github.com/szechyjs/mbelib
#Git-Clone:     https://github.com/szechyjs/mbelib.git
Source:         https://github.com/szechyjs/mbelib/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:  gcc-c++
Requires:	pkgconfig

%description
mbelib supports the 7200x4400 bit/s codec used in P25 Phase 1,
the 7100x4400 bit/s codec used in ProVoice and the "Half Rate"
3600x2250 bit/s vocoder used in various radio systems.

%package devel
Summary:        Development headers for mbelib
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mbelib

%global debug_package %{nil}

%prep
%autosetup

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="lib64"
%cmake_build

%install
make -C build install DESTDIR=%{buildroot}
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

%clean
rm -rf $RPM_BUILD_ROOT/

%files
%doc README.md COPYRIGHT CHANGELOG
%{_libdir}/libmbe.so
%{_libdir}/libmbe.a
%{_libdir}/libmbe.so*

%files devel
%{_includedir}/mbelib.h

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec

