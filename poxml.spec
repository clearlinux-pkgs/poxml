#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : poxml
Version  : 24.08.2
Release  : 70
URL      : https://download.kde.org/stable/release-service/24.08.2/src/poxml-24.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.2/src/poxml-24.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.2/src/poxml-24.08.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: poxml-bin = %{version}-%{release}
Requires: poxml-license = %{version}-%{release}
Requires: poxml-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gettext-dev
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the poxml package.
Group: Binaries
Requires: poxml-license = %{version}-%{release}

%description bin
bin components for the poxml package.


%package license
Summary: license components for the poxml package.
Group: Default

%description license
license components for the poxml package.


%package man
Summary: man components for the poxml package.
Group: Default

%description man
man components for the poxml package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n poxml-24.08.2
cd %{_builddir}/poxml-24.08.2
pushd ..
cp -a poxml-24.08.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728571680
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728571680
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/poxml
cp %{_builddir}/poxml-%{version}/COPYING %{buildroot}/usr/share/package-licenses/poxml/a21ac62aee75f8fcb26b1de6fc90e5eea271854c || :
cp %{_builddir}/poxml-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/poxml/fcbf818f92ef8679a88f3778b12b4c8b5810545b || :
cp %{_builddir}/poxml-%{version}/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/poxml/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/po2xml
/V3/usr/bin/split2po
/V3/usr/bin/swappo
/V3/usr/bin/xml2pot
/usr/bin/po2xml
/usr/bin/split2po
/usr/bin/swappo
/usr/bin/xml2pot

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/poxml/a21ac62aee75f8fcb26b1de6fc90e5eea271854c
/usr/share/package-licenses/poxml/fcbf818f92ef8679a88f3778b12b4c8b5810545b
/usr/share/package-licenses/poxml/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/po2xml.1
/usr/share/man/ca/man1/split2po.1
/usr/share/man/ca/man1/swappo.1
/usr/share/man/ca/man1/xml2pot.1
/usr/share/man/da/man1/po2xml.1
/usr/share/man/da/man1/split2po.1
/usr/share/man/da/man1/swappo.1
/usr/share/man/da/man1/xml2pot.1
/usr/share/man/de/man1/po2xml.1
/usr/share/man/de/man1/split2po.1
/usr/share/man/de/man1/swappo.1
/usr/share/man/de/man1/xml2pot.1
/usr/share/man/es/man1/po2xml.1
/usr/share/man/es/man1/split2po.1
/usr/share/man/es/man1/swappo.1
/usr/share/man/es/man1/xml2pot.1
/usr/share/man/et/man1/split2po.1
/usr/share/man/fr/man1/po2xml.1
/usr/share/man/fr/man1/split2po.1
/usr/share/man/fr/man1/swappo.1
/usr/share/man/fr/man1/xml2pot.1
/usr/share/man/gl/man1/po2xml.1
/usr/share/man/gl/man1/split2po.1
/usr/share/man/gl/man1/swappo.1
/usr/share/man/gl/man1/xml2pot.1
/usr/share/man/it/man1/po2xml.1
/usr/share/man/it/man1/split2po.1
/usr/share/man/it/man1/swappo.1
/usr/share/man/it/man1/xml2pot.1
/usr/share/man/man1/po2xml.1
/usr/share/man/man1/split2po.1
/usr/share/man/man1/swappo.1
/usr/share/man/man1/xml2pot.1
/usr/share/man/nl/man1/po2xml.1
/usr/share/man/nl/man1/split2po.1
/usr/share/man/nl/man1/swappo.1
/usr/share/man/nl/man1/xml2pot.1
/usr/share/man/pt/man1/po2xml.1
/usr/share/man/pt/man1/split2po.1
/usr/share/man/pt/man1/swappo.1
/usr/share/man/pt/man1/xml2pot.1
/usr/share/man/pt_BR/man1/po2xml.1
/usr/share/man/pt_BR/man1/split2po.1
/usr/share/man/pt_BR/man1/swappo.1
/usr/share/man/pt_BR/man1/xml2pot.1
/usr/share/man/ru/man1/po2xml.1
/usr/share/man/ru/man1/split2po.1
/usr/share/man/ru/man1/swappo.1
/usr/share/man/ru/man1/xml2pot.1
/usr/share/man/sl/man1/po2xml.1
/usr/share/man/sl/man1/split2po.1
/usr/share/man/sl/man1/swappo.1
/usr/share/man/sl/man1/xml2pot.1
/usr/share/man/sv/man1/po2xml.1
/usr/share/man/sv/man1/split2po.1
/usr/share/man/sv/man1/swappo.1
/usr/share/man/sv/man1/xml2pot.1
/usr/share/man/uk/man1/po2xml.1
/usr/share/man/uk/man1/split2po.1
/usr/share/man/uk/man1/swappo.1
/usr/share/man/uk/man1/xml2pot.1
