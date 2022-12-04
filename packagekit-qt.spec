%define api 5
%define major 1
%define binname packagekitqt
%define libname %mklibname %{binname} %{api} %{major}
%define devname %mklibname -d %{binname} %{api}

Summary:	A DBUS packaging abstraction layer
Name:		packagekit-qt
Version:	1.1.0
Release:	1
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://www.packagekit.org
Source0:	https://github.com/hughsie/PackageKit-Qt/releases/download/v%{version}/PackageKit-Qt-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	packagekit >= %{version}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	qmake5
Requires:	packagekit >= %{version}

%description
PackageKit is a DBUS abstraction layer that allows the session user to manage
packages in a secure way using a cross-distro, cross-architecture API.

%package -n %{libname}
Summary:	Libraries for accessing PackageKit-Qt5
Group:		System/Configuration/Packaging
Requires:	packagekit >= %{version}

%description -n %{libname}
Libraries for accessing PackageKit-Qt5.

%package -n %{devname}
Summary:	Libraries and headers for PackageKit-Qt5
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	packagekit-devel < %{version}

%description -n %{devname}
Headers and libraries for PackageKit-Qt5.

%prep
%autosetup -n PackageKit-Qt-%{version} -p1

%build
%cmake -DUSE_QT5:BOOL=ON
%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/lib%{binname}%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{binname}%{api}
%{_libdir}/lib%{binname}%{api}.so
%{_libdir}/pkgconfig/packagekitqt%{api}.pc
%{_libdir}/cmake/%{binname}%{api}
