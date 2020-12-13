Name:           libmirisdr
Version:        1.1.2
Release:        1%{?dist}
Summary:        Support programs for MRi2500
License:        GPL-2.0
Group:          Productivity/Hamradio/Other
Url:            https://github.com/f4exb/libmirisdr-4
Source:         https://github.com/f4exb/libmirisdr-4/archive/%{version}/libmirisdr-4-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Programs that controls Mirics MRi2500 based DVB dongle in raw mode, so
it can be used as a SDR receiver.

%package devel
Summary:        Development files for libmirisdr
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Library headers and other development files for mirisdr driver.

%package udev
Summary:        Udev rules for Mirics MRi2500 based DVB dongles
Group:          Hardware/Other

%description udev
Udev rules for Mirics MRi2500 based DVB dongles.

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/libmirisdr.a

#install udev rules
install -D -p -m 0644 mirisdr.rules %{buildroot}%{_udevrulesdir}/10-mirisdr.rules

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/libmirisdr.so*
%{_bindir}/miri_fm
%{_bindir}/miri_sdr

%files udev
%defattr(-,root,root)
%{_udevrulesdir}/10-mirisdr.rules

%files devel
%defattr(-,root,root)
%{_libdir}/libmirisdr.so
%{_includedir}/mirisdr.h
%{_includedir}/mirisdr_export.h
%{_libdir}/pkgconfig/libmirisdr.pc

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec
