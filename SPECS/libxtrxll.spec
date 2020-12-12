%global commit 1b6eddfbedc700efb6f7e3c3594e43ac6ff29ea4
%global short %(c=%{commit}; echo ${c:0:10})
%global date 221202
%define xtrx_group xtrx
Name:           libxtrxll
Version:        0
Release:        0.%{date}git%{short}%{?dist}
Summary:        XTRX Low-level API library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://xtrx.io
#Git-Clone:     https://github.com/xtrx-sdr/libxtrxll.git
Source:         https://github.com/xtrx-sdr/libxtrxll.git/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         libxtrxll-fix-udev-permissions.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libusb3380-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libusb3380)

%description
Low level XTRX hardware abstraction library.
Requires:       xtrx-usb-udev

%package devel
Summary:        XTRX Low-level API library - devel
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Low level XTRX hardware abstraction library.

This subpackage contains libraries and header files for developing
applications that want to make use of libxtrxll.

%package tools
Summary:        Low level tools for XTRX
Group:          Hardware/Other

%description tools
Low level tools for XTRX SDR devices.

%package usb-udev
Summary:        Udev rules for XTRX USB devices
Group:          Hardware/Other
BuildArch:      noarch

%description usb-udev
Udev rules for XTRX USB devices.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="" \
    -DFORCE_ARCH=x86_64 \
    -DENABLE_PCIE=ON \
    -DENABLE_USB3380=ON \
    -DINSTALL_UDEV_RULES=ON \
    -DUDEV_RULES_PATH=/etc/udev/rules.d
%make_build

%install
%cmake_install
install -d %{buildroot}/%{_bindir}
mv %{buildroot}%{_libdir}/xtrxll/test_xtrxflash %{buildroot}/%{_bindir}
mv %{buildroot}%{_libdir}/xtrxll/test_xtrxll %{buildroot}/%{_bindir}

%pre usb-udev
getent group %{xtrx_group} >/dev/null || groupadd -r %{xtrx_group}

%post usb-udev
%udev_rules_update

%postun usb-udev
%udev_rules_update

%files
%license LICENSE
%doc README.md
%{_libdir}/libxtrxll.so*

%files devel
%{_includedir}/xtrxll_*.h
%{_libdir}/libxtrxll.so
%{_libdir}/pkgconfig/libxtrxll.pc

%files tools
%{_bindir}/test_xtrxflash
%{_bindir}/test_xtrxll

%files usb-udev
/etc/udev/rules.d/*.rules

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec
