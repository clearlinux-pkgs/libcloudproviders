#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : libcloudproviders
Version  : 0.3.2
Release  : 3
URL      : https://gitlab.gnome.org/World/libcloudproviders/-/archive/0.3.2/libcloudproviders-0.3.2.tar.gz
Source0  : https://gitlab.gnome.org/World/libcloudproviders/-/archive/0.3.2/libcloudproviders-0.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: libcloudproviders-data = %{version}-%{release}
Requires: libcloudproviders-lib = %{version}-%{release}
Requires: libcloudproviders-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# cloudproviders integration API
libcloudproviders is a DBus API that allows cloud storage sync clients to expose
their services. Clients such as file managers and desktop environments can then
provide integrated access to the cloud providers services.

%package data
Summary: data components for the libcloudproviders package.
Group: Data

%description data
data components for the libcloudproviders package.


%package dev
Summary: dev components for the libcloudproviders package.
Group: Development
Requires: libcloudproviders-lib = %{version}-%{release}
Requires: libcloudproviders-data = %{version}-%{release}
Provides: libcloudproviders-devel = %{version}-%{release}
Requires: libcloudproviders = %{version}-%{release}

%description dev
dev components for the libcloudproviders package.


%package lib
Summary: lib components for the libcloudproviders package.
Group: Libraries
Requires: libcloudproviders-data = %{version}-%{release}
Requires: libcloudproviders-license = %{version}-%{release}

%description lib
lib components for the libcloudproviders package.


%package license
Summary: license components for the libcloudproviders package.
Group: Default

%description license
license components for the libcloudproviders package.


%prep
%setup -q -n libcloudproviders-0.3.2
cd %{_builddir}/libcloudproviders-0.3.2
pushd ..
cp -a libcloudproviders-0.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691601548
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libcloudproviders
cp %{_builddir}/libcloudproviders-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libcloudproviders/f45ee1c765646813b442ca58de72e20a64a7ddba || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/CloudProviders-0.3.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/cloudproviders.deps
/usr/share/vala/vapi/cloudproviders.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/cloudproviders/cloudproviders.h
/usr/include/cloudproviders/cloudprovidersaccount.h
/usr/include/cloudproviders/cloudprovidersaccountexporter.h
/usr/include/cloudproviders/cloudproviderscollector.h
/usr/include/cloudproviders/cloudprovidersprovider.h
/usr/include/cloudproviders/cloudprovidersproviderexporter.h
/usr/include/cloudproviders/enums.h
/usr/lib64/libcloudproviders.so
/usr/lib64/pkgconfig/cloudproviders.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libcloudproviders.so.0.3.2
/usr/lib64/libcloudproviders.so.0
/usr/lib64/libcloudproviders.so.0.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcloudproviders/f45ee1c765646813b442ca58de72e20a64a7ddba
