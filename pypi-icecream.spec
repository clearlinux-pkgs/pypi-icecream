#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v3
# autospec commit: 750e50d
#
Name     : pypi-icecream
Version  : 2.1.3
Release  : 4
URL      : https://files.pythonhosted.org/packages/1c/8b/ae6ebc9fc423f9397a0982990c86f1fe94077df729ef452c9a847fb16ae6/icecream-2.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/1c/8b/ae6ebc9fc423f9397a0982990c86f1fe94077df729ef452c9a847fb16ae6/icecream-2.1.3.tar.gz
Summary  : Never use print() to debug again; inspect variables, expressions, and program execution with a single, simple function call.
Group    : Development/Tools
License  : MIT
Requires: pypi-icecream-license = %{version}-%{release}
Requires: pypi-icecream-python = %{version}-%{release}
Requires: pypi-icecream-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(asttokens)
BuildRequires : pypi(colorama)
BuildRequires : pypi(executing)
BuildRequires : pypi(pygments)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<h1 align="center">
<img src="logo.svg" width="220px" height="370px" alt="icecream">
</h1>

%package license
Summary: license components for the pypi-icecream package.
Group: Default

%description license
license components for the pypi-icecream package.


%package python
Summary: python components for the pypi-icecream package.
Group: Default
Requires: pypi-icecream-python3 = %{version}-%{release}

%description python
python components for the pypi-icecream package.


%package python3
Summary: python3 components for the pypi-icecream package.
Group: Default
Requires: python3-core
Provides: pypi(icecream)
Requires: pypi(asttokens)
Requires: pypi(colorama)
Requires: pypi(executing)
Requires: pypi(pygments)

%description python3
python3 components for the pypi-icecream package.


%prep
%setup -q -n icecream-2.1.3
cd %{_builddir}/icecream-2.1.3
pushd ..
cp -a icecream-2.1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707121718
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
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 setup.py build

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
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-icecream
cp %{_builddir}/icecream-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-icecream/b8f86765976b32656e96e11a7ccb328dafd128fc || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-icecream/b8f86765976b32656e96e11a7ccb328dafd128fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
