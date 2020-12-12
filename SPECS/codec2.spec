%global commit 59722eb3e5bf3b4533b45cbf1a6a7b55cce15ddb
%global short %(c=%{commit}; echo ${c:0:10})
%global date 20191111
Name:           codec2
Version:        0.9.2
Release:        0.%{date}git%{short}%{?dist}
Summary:        Low bit rate speech codec
License:        LGPL-2.1-only
Group:          Productivity/Hamradio/Other
URL:            https://rowetel.com/codec2.html
Source:         https://github.com/drowe67/codec2/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libsamplerate-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel

%description
Codec 2 is an open source (LGPL licensed) speech codec for 2400 bit/s
and below. This is the runtime library package.

%package devel
Summary:        Development files for Codec 2 
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Codec 2 is an open source (LGPL licensed) speech codec for 2400 bit/s
and below. This package contains the development files required to 
compile programs that use codec2.

%package devel-examples
Summary:        Example code for Codec 2
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
BuildArch:      noarch

%description devel-examples
Example code for Codec 2

%prep
%autosetup

%build
rm -rf build_linux && mkdir build_linux && pushd build_linux
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    ../

%cmake_build


%install
pushd build_linux
%make_install
popd

# Create and install pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/codec2.pc << EOF
prefix=%{_prefix}
exec_prefix=\${prefix}
includedir=\${prefix}/include/%{name}
libdir=\${exec_prefix}/%{_lib}

Name: codec2
Description: Next-Generation Digital Voice for Two-Way Radio
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -l%{name}
EOF

%files
%license COPYING
%doc README*
%{_bindir}/c2dec
%{_bindir}/c2enc
%{_bindir}/drs232
%{_bindir}/drs232_ldpc
%{_bindir}/fdmdv_demod
%{_bindir}/fdmdv_get_test_bits
%{_bindir}/fdmdv_mod
%{_bindir}/fdmdv_put_test_bits
%{_bindir}/fsk_mod
%{_bindir}/fm_demod
%{_bindir}/insert_errors
%{_libdir}/libcodec2.so.*

%files devel
%{_includedir}/*
%dir %{_libdir}/cmake/codec2
%{_libdir}/cmake/codec2/codec2-config-relwithdebinfo.cmake
%{_libdir}/cmake/codec2/codec2-config.cmake
%{_libdir}/libcodec2.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Dec 09 2020 lu3vea@gmail.com
- First Fedora spec

