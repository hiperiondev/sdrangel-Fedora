%define bladerf_group bladerf
Name:           bladeRF
Version:        2019.07
Release:        1%{?dist} 
Summary:        SDR radio receiver
License:        GPL-2.0-only AND AGPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://nuand.com/
#Git-Clone:     https://github.com/Nuand/bladeRF.git
Source0:        https://github.com/Nuand/bladeRF/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.4
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(udev)

# Although the build scripts mangle the version number to be RPM compatible
# for continuous builds (transforming the output of `git describe`), Fedora 32+
# also validates the version inside the pkgconfig file. There's no impetus for this
# with fish.
%define _wrong_version_format_terminate_build 0

%description
The software for bladeRF USB 3.0 Superspeed Software Defined Radio.

%package libs
Summary:        SDR radio receiver library
Group:          System/Libraries
Version:       %{version}
Release:        41.8
Requires:       udev

%description libs
Library for bladeRF, an SDR transceiver.

%package doc
Summary:        Documentation for libbladeRF
Group:          Documentation/HTML
Version:        %{version}
Release:        41.8

%description doc
HTML documentation files for libbladeRF.

%package udev
Summary:        Udev rules for bladeRF
Group:          Hardware/Other

%description udev
Udev rules for bladeRF.

%package devel
Summary:        Development files for libbladeRF
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for developing applications that want to make
use of libbladerf.

%prep
%autosetup

%build
cd host
%cmake \
  -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
  -DUDEV_RULES_PATH=%{_udevrulesdir} \
  -DBLADERF_GROUP=%{bladerf_group} \
%if 0%{?use_syslog}
  -DENABLE_LIBBLADERF_SYSLOG=ON \
%endif
  -DBUILD_DOCUMENTATION=ON
%cmake_build

%install
cd host
%cmake_install

#move docs
mkdir -p %{buildroot}%{_docdir}

%pre udev
getent group %{bladerf_group} >/dev/null || groupadd -r %{bladerf_group}

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

mv %{buildroot}/lib %{buildroot}/lib64

%files
%license COPYING
%doc README.md CONTRIBUTORS
%{_bindir}/bladeRF-cli
%{_bindir}/bladeRF-fsk
%{_mandir}/man1/bladeRF-cli.1.gz
%files udev
%{_udevrulesdir}/88-nuand-*.rules

%files libs
%{_libdir}/libbladeRF.so*

%files libs
%{_docdir}/libbladeRF

%files devel
%{_libdir}/libbladeRF.so*
%{_includedir}/bladeRF1.h
%{_includedir}/bladeRF2.h
%{_includedir}/libbladeRF.h
%{_libdir}/pkgconfig/libbladeRF.pc

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com - 2019.07-1
- First Fedora spec
