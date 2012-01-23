%define major  1
%define libname %mklibname qtbamf %{major}
%define develname %mklibname qtbamf -d

Summary:	Qt binding and QML plugin for bamf
Name:		libqtbamf
Version:	0.2.2
Release:	1
License:	LGPLv3,GPLv3
Url:		http://launchpad.net/bamf-qt
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - libqtbamf-cmake-libdir-fix.patch nmarques@opensuse.org -- Fixes $LIBDIR for file installation, upstreamed (lp#784262)
Patch0:		libqtbamf-cmake-libdir-fix.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtDeclarative)

%description
Qt binding and QML plugin for the bamf dbus daemon semi-automatically
generated with qdbusxml2cpp and matching the GObject library structure.

%package -n %{libname}
Summary:	Qt binding and QML plugin for bamf - shared libraries
Group:		System/Libraries

%description -n %{libname}
Qt binding and QML plugin for the bamf dbus daemon semi-automatically
generated with qdbusxml2cpp and matching the GObject library structure.

%package -n %{develname}
Summary:	Qt binding and QML plugin for bamf - development files
Group:		Development/C++
Requires:	%{libname} = %{version}

%description -n %{develname}
Qt binding and QML plugin for the bamf dbus daemon semi-automatically
generated with qdbusxml2cpp and matching the GObject library structure.

%prep
%setup -q
%apply_patches

%build
#pushd build
export BUILD_GLOBAL=true
%cmake \
	-Dlibdir=%{_libdir} \

%make

%install
pushd build
# .pc file hack
sed -i 's/libdir=\${exec_prefix}\/lib/libdir=\${exec_prefix}\/%{_lib}/g' ../libqtbamf.pc
%makeinstall_std
popd build

%files -n %{libname}
%doc COPYING-GPL3 COPYING-LGPL3 README
%{_libdir}/*.so.%{major}*
%{_libdir}/qt4/plugins/imports/bamf/

%files -n %{develname}
%{_includedir}/QtBamf/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libqtbamf.pc

