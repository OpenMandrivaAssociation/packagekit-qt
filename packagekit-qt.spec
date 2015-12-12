%define api 4
%define major 0
%define binname packagekitqt
%define libname %mklibname %{binname} %{api} %{major}
%define devname %mklibname -d %{name}
%define libname5 %mklibname %{binname}5 %{major}
%define devname5 %mklibname -d %{binname}5

%bcond_without qt4
%bcond_without qt5

Summary:	A DBUS packaging abstraction layer
Name:		packagekit-qt
Version:	0.9.5
Release:	8
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://www.packagekit.org
Source0:	http://www.freedesktop.org/software/PackageKit/releases/PackageKit-Qt-%{version}.tar.xz
Patch0:		PackageKit-Qt-0.9.5-use-full-cmakedirs.patch
# (tpg) patches from upstream git
Patch1:		0001-Make-use-of-QLoggingCategory-packagekitqt.patch
Patch2:		0002-Fix-copy-n-paste-typo.patch
Patch3:		0003-Fix-compilation-with-strict-QString-constructors-on-.patch
Patch4:		0004-Move-enumTo-FromString-code-from-header-to-cpp-file.patch

BuildRequires:	cmake
BuildRequires:	packagekit >= %{version}
%if %{with qt4}
BuildRequires:	pkgconfig(QtCore)
%endif
%if %{with qt5}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	qmake5
%endif
Requires:	packagekit >= %{version}

%description
PackageKit is a DBUS abstraction layer that allows the session user to manage
packages in a secure way using a cross-distro, cross-architecture API.

%if %{with qt4}
%package -n	%{libname}
Summary:	Libraries for accessing PackageKit-Qt
Group:		System/Configuration/Packaging
Requires:	packagekit >= %{version}

%description -n	%{libname}
Libraries for accessing PackageKit-Qt.

%package -n	%{devname}
Summary:	Libraries and headers for PackageKit
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	packagekit-devel < %{version}

%description -n %{devname}
Headers and libraries for PackageKit.
%endif

%if %{with qt5}
%package -n	%{libname5}
Summary:	Libraries for accessing PackageKit-Qt5
Group:		System/Configuration/Packaging
Requires:	packagekit >= %{version}

%description -n	%{libname5}
Libraries for accessing PackageKit-Qt5.

%package -n	%{devname5}
Summary:	Libraries and headers for PackageKit-Qt5
Group:		Development/Other
Requires:	%{libname5} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	packagekit-devel < %{version}

%description -n %{devname5}
Headers and libraries for PackageKit-Qt5.
%endif

%prep
%setup -qn PackageKit-Qt-%{version}
%apply_patches

%build
%if %{with qt4}
%cmake
%make
cd ..
mv build build-qt4
%endif

%if %{with qt5}
%cmake -DUSE_QT5:BOOL=ON
%make
cd ..
mv build build-qt5
%endif

%install
%if %{with qt4}
ln -s build-qt4 build
%makeinstall_std -C build
rm build
%endif
%if %{with qt5}
ln -s build-qt5 build
%makeinstall_std -C build
%endif

%if %{with qt4}
%files -n %{libname}
%{_libdir}/lib%{binname}%{api}.so.%{major}
%{_libdir}/lib%{binname}%{api}.so.%{version}

%files -n %{devname}
%{_includedir}/%{binname}%{api}/PackageKit
%{_libdir}/lib%{binname}%{api}.so
%{_libdir}/pkgconfig/packagekitqt%{api}.pc
%{_libdir}/cmake/%{binname}%{api}
%endif

%if %{with qt5}
%files -n %{libname5}
%{_libdir}/lib%{binname}5.so.%{major}*

%files -n %{devname5}
%{_includedir}/%{binname}5
%{_libdir}/lib%{binname}5.so
%{_libdir}/pkgconfig/packagekitqt5.pc
%{_libdir}/cmake/%{binname}5
%endif
