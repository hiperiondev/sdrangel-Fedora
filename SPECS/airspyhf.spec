Name:           airspyhf
Version:        1.6.8
Release:        1%{?dist}
Summary:        Support programs for Airspy HF+ SDR
License:        BSD-3-Clause
URL:            http://www.airspy.com/airspy-hf-plus
#Git-Clone:     https://github.com/airspy/airspyhf.git
Source:         https://github.com/airspy/%{name}/archive/%{version}/%{name}-%{version}.tar.gz         
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(udev)

%description
Host software for Airspy HF+, a software defined radio
for the HF and VHF bands.

%package libs
Summary:        Driver for Airspy HF+
Requires:       %{name}-udev

%description libs
Library to run Airspy HF+ SDR receiver.

%package udev
Summary:        Udev rules for Airspy HF+ SDR
#Requires(pre):  shadow

%description udev
Udev rules for Airspy HF+ SDR.

%package devel
Summary:        Development files for Airspy HF+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Library headers for Airspy HF+ driver.

%package doc
Summary:        Documentation for Airspy HF+

%description doc
Documentation for Airspy HF+ driver.

%prep
%autosetup

# HACK: set udev group to airspyhf
sed -i "s/plugdev/airspyhf/g" tools/52-airspyhf.rules

%build
%cmake -DINSTALL_UDEV_RULES=ON

%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/libairspyhf.a

mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspyhf.rules %{buildroot}%{_udevrulesdir}

%pre udev
getent group airspyhf_group >/dev/null || groupadd -r airspyhf_group

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files
%{_bindir}/airspyhf_calibrate
%{_bindir}/airspyhf_gpio
%{_bindir}/airspyhf_info
%{_bindir}/airspyhf_lib_version
%{_bindir}/airspyhf_rx

%files libs
%license LICENSE
%{_libdir}/libairspyhf.so.*

%files udev
%{_udevrulesdir}/52-airspyhf.rules

%files devel
%{_libdir}/libairspyhf.so
%{_includedir}/libairspyhf
%{_libdir}/pkgconfig/libairspyhf.pc

%files doc
%doc README.md

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec
