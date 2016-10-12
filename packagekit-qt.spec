%define api 5
%define major 0
%define binname packagekitqt
%define libname %mklibname %{binname} %{api} %{major}
%define devname %mklibname -d %{binname} %{api}

Summary:	A DBUS packaging abstraction layer
Name:		packagekit-qt
Version:	0.9.6
Release:	1
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://www.packagekit.org
Source0:	http://www.freedesktop.org/software/PackageKit/releases/PackageKit-Qt-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	packagekit >= %{version}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	qmake5
Requires:	packagekit >= %{version}

%description
PackageKit is a DBUS abstraction layer that allows the session user to manage
packages in a secure way using a cross-distro, cross-architecture API.

%package -n	%{libname}
Summary:	Libraries for accessing PackageKit-Qt
Group:		System/Configuration/Packaging
Requires:	packagekit >= %{version}
Obsoletes:	%{mklibname packagekitqt 4 0} < 0.9.6

%description -n	%{libname}
Libraries for accessing PackageKit-Qt.

%package -n	%{devname}
Summary:	Libraries and headers for PackageKit
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	packagekit-devel < %{version}
Obsoletes:	%{mklibname packagekitqt -d} < 0.9.6

%description -n %{devname}
Headers and libraries for PackageKit.

%prep
%setup -qn PackageKit-Qt-%{version}
%apply_patches

%cmake_qt5 -DUSE_QT5:BOOL=ON

%build
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/lib%{binname}5.so.%{major}*

%files -n %{devname}
%{_includedir}/%{binname}5
%{_libdir}/lib%{binname}5.so
%{_libdir}/pkgconfig/packagekitqt5.pc
%{_libdir}/cmake/%{binname}5
