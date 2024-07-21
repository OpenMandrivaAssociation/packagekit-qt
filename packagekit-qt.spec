%define api 5
%define major 1
%define binname packagekitqt
%define libname %mklibname %{binname} %{api}
%define devname %mklibname -d %{binname} %{api}
%define q6binname packagekitqt6
%define q6libname %mklibname %{q6binname} %{api}
%define q6devname %mklibname -d %{q6binname} %{api}

Summary:	A DBUS packaging abstraction layer
Name:		packagekit-qt
Version:	1.1.2
Release:	1
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://www.packagekit.org
Source0:	https://github.com/PackageKit/PackageKit-Qt/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	packagekit >= %{version}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	qmake5
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
Requires:	packagekit >= %{version}

%description
PackageKit is a DBUS abstraction layer that allows the session user to manage
packages in a secure way using a cross-distro, cross-architecture API.

%package -n %{libname}
Summary:	Libraries for accessing PackageKit-Qt5
Group:		System/Configuration/Packaging
Requires:	packagekit >= %{version}
%define oldlibname %mklibname %{binname} %{api} %{major}
%rename %{oldlibname}

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

%package -n %{q6libname}
Summary:	Libraries for accessing PackageKit-Qt6
Group:		System/Configuration/Packaging
Requires:	packagekit >= %{version}

%description -n %{q6libname}
Libraries for accessing PackageKit-Qt6.

%package -n %{q6devname}
Summary:	Libraries and headers for PackageKit-Qt6
Group:		Development/Other
Requires:	%{q6libname} = %{EVRD}
Provides:	%{name}6-devel = %{EVRD}

%description -n %{q6devname}
Headers and libraries for PackageKit-Qt6.

%prep
%autosetup -n PackageKit-Qt-%{version} -p1
%cmake \
	-DBUILD_WITH_QT6:BOOL=OFF \
	-G Ninja
cd ..

export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DBUILD_WITH_QT6:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%ninja_build -C build-qt6

%install
%ninja_install -C build

%ninja_install -C build-qt6

%files -n %{libname}
%{_libdir}/lib%{binname}%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{binname}%{api}
%{_libdir}/lib%{binname}%{api}.so
%{_libdir}/pkgconfig/packagekitqt%{api}.pc
%{_libdir}/cmake/%{binname}%{api}

%files -n %{q6libname}
%{_libdir}/libpackagekitqt6.so.%{major}*

%files -n %{q6devname}
%{_includedir}/packagekitqt6
%{_libdir}/libpackagekitqt6.so
%{_libdir}/pkgconfig/packagekitqt6.pc
%{_libdir}/cmake/packagekitqt6
