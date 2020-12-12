Name:           dsdcc
Version:        1.9.0
Release:        1%{?dist}
Summary:        Digital Speech Decoder (DSD) rewritten as a C++ library
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://github.com/f4exb/dsdcc
#Git-Clone:     https://github.com/f4exb/dsdcc.git
Source:         https://github.com/f4exb/dsdcc/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
DSDcc is a complete rewrite from the original DSD (Digital Speech Decoder) project.
It provides a binary executable dsdccx and a library libdsdcc.so to be used in
other programs.
It decodes DMR, dPMR, D-Star and Yaesu System Fusion (YSF) standards.

%package libs
Summary:        Digital Speech Decoder (DSD) rewritten as a C++ library
Group:          System/Libraries

%description libs
DSDcc is a complete rewrite from the original DSD (Digital Speech Decoder) project.
It provides a binary executable dsdccx and a library libdsdcc.so to be used in
other programs.
It decodes DMR, dPMR, D-Star and Yaesu System Fusion (YSF) standards.

This subpackage contains the shared library files for libdsdcc.

%package devel
Summary:        Development files for the dsdcc library
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
DSDcc is a complete rewrite from the original DSD (Digital Speech Decoder) project.
It provides a binary executable dsdccx and a library libdsdcc.so to be used in
other programs.
It decodes DMR, dPMR, D-Star and Yaesu System Fusion (YSF) standards.

This subpackage contains libraries and header files for developing
applications that want to make use of libdsdcc.

%prep
%autosetup

%build
%cmake \
  -DUSE_MBELIB=OFF \
  -Wno-dev
%make_build

%install
%cmake_install

%files
%doc messagefile.md Readme.md
%{_bindir}/dsdccx*

%files libs
%{_libdir}/libdsdcc.so*

%files devel
%{_includedir}/dsdcc
%{_libdir}/libdsdcc.so
%{_libdir}/pkgconfig/libdsdcc.pc

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec
