%define perseussdr_group perseususb
Name:           libperseus-sdr
Version:        0.8.2
Release:        1%{?dist}
Summary:        Perseus Software Defined Radio Control Library
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/Microtelecom/libperseus-sdr
#Git-Clone:     https://github.com/Microtelecom/libperseus-sdr.git
Source:         https://github.com/Microtelecom/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vim
BuildRequires:  libusbx-devel
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(udev)
Requires:       udev

%description
Perseus Software Defined Radio Control Library.

%package devel
Summary:        Development files for libperseus-sdr
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for developing applications that want to
make use of libperseus-sdr.

%package tools
Summary:        Tools for Perseus SDR
Group:          Hardware/Other

%description tools
Tools for Perseus SDR devices.

%package udev
Summary:        Udev rules for Perseus SDR
Group:          Hardware/Other

%description udev
Udev rules for Perseus SDR hardware

%prep
%autosetup
#
%build
# Do not optimize for current cpu
sed -i "s|-march=native||g" configure.ac
autoreconf -iv
%configure
%make_build 

%install
%make_install
install -Dm0644 95-perseus.rules %{buildroot}%{_udevrulesdir}/95-perseus.rules
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64 
cp %{_builddir}/%{name}-%{version}/*.h %{buildroot}/%{_includedir}
rm %{buildroot}/%{_bindir}/*

%pre udev
getent group %{perseussdr_group} >/dev/null || groupadd -r %{perseussdr_group}

%files
%doc AUTHORS README.md
%license COPYING.LESSER
%{_libdir}/libperseus-sdr.so*
%{_libdir}/pkgconfig/libperseus-sdr.pc

%files tools

%files udev
%{_libdir}/lib/udev/rules.d/95-perseus.rules

%files devel
%{_libdir}/libperseus-sdr.so
%{_includedir}/perseus-sdr.h
%{_includedir}/perseus-in.h
%{_includedir}/perseus-sdr.h
%{_includedir}/perseusfx2.h
%{_includedir}/config.h
%{_includedir}/fpga_data.h

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec
