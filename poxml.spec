#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : poxml
Version  : 19.08.3
Release  : 13
URL      : https://download.kde.org/stable/applications/19.08.3/src/poxml-19.08.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.3/src/poxml-19.08.3.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.3/src/poxml-19.08.3.tar.xz.sig
Summary  : Translates DocBook XML files using gettext po files
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: poxml-bin = %{version}-%{release}
Requires: poxml-license = %{version}-%{release}
Requires: poxml-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gettext-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n poxml-19.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573196478
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573196478
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/poxml
cp %{_builddir}/poxml-19.08.3/COPYING %{buildroot}/usr/share/package-licenses/poxml/a21ac62aee75f8fcb26b1de6fc90e5eea271854c
cp %{_builddir}/poxml-19.08.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/poxml/fcbf818f92ef8679a88f3778b12b4c8b5810545b
cp %{_builddir}/poxml-19.08.3/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/poxml/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/man/sv/man1/po2xml.1
/usr/share/man/sv/man1/split2po.1
/usr/share/man/sv/man1/swappo.1
/usr/share/man/sv/man1/xml2pot.1
/usr/share/man/uk/man1/po2xml.1
/usr/share/man/uk/man1/split2po.1
/usr/share/man/uk/man1/swappo.1
/usr/share/man/uk/man1/xml2pot.1
