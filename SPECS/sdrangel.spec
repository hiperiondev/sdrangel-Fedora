# Don't build with LTO since it breaks sdrangel
%define _lto_cflags %{nil}

%ifarch %{ix86} %{arm}
%bcond_with    fec
%else
%bcond_without fec
%endif
%bcond_without freedv
Name:           sdrangel
Version:        6.5.0
Release:        1%{?dist}
Summary:        SDR/Analyzer frontend for Airspy, BladeRF, HackRF, RTL-SDR and FunCube
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://github.com/f4exb/sdrangel
Source:         https://github.com/f4exb/sdrangel/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  dsdcc-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  boost-devel
BuildRequires:  LimeSuite-devel
BuildRequires:  serialDV-devel
BuildRequires:  airspyone_host-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libxtrxll-devel
BuildRequires:  rpmfusion-free-release
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(codec2)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(libairspyhf)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libbladeRF)
BuildRequires:  pkgconfig(libhackrf)
BuildRequires:  pkgconfig(libiio)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(libpostproc)
# It does not build with libmirisdr from upstream
# https://github.com/f4exb/libmirisdr-4 is needed
#BuildRequires:  pkgconfig(libmirisdr)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxtrxll)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(libswscale)
Requires:       python3-requests
%if 0%{with fec}
BuildRequires:  pkgconfig(libcm256cc)
BuildRequires:  pkgconfig(nanomsg)
%endif
%if 0%{with freedv}
BuildRequires:  pkgconfig(codec2)
%endif

%description
SDRangel is an Open Source Qt5/OpenGL SDR and signal analyzer frontend
to various hardware.

%package doc
Summary:        Documentation for SDRangel

%description doc
Documentation for SDRangel

%prep
%autosetup
sed -i 's/\r$//' Readme.md
sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|g' swagger/sdrangel/examples/*.py

%build
export CXXFLAGS="%{optflags} -Wno-return-type -fpermissive"
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_DISTRIBUTION=ON \
  -DFORCE_SSE41=ON \
  -DRX_SAMPLE_24BIT=ON
%make_build

%install
%cmake_install
rm -f %{buildroot}%{_datadir}/sdrangel/Readme.md

%files
%license LICENSE
%{_bindir}/sdrangel
%{_bindir}/sdrangelbench
%{_bindir}/sdrangelsrv
%dir %{_prefix}/lib/sdrangel
%{_prefix}/lib/sdrangel/lib*
%{_prefix}/lib/sdrangel/plugins
%{_prefix}/lib/sdrangel/pluginssrv
%{_datadir}/applications/sdrangel.desktop
%{_datadir}/icons/hicolor/scalable/apps/sdrangel_icon.svg

%files doc
%doc Readme.md
%doc swagger/sdrangel/examples/

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com - 6.5.0-1
- First Fedora spec
