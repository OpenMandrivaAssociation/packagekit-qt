%define	api	2
%define	major	5
%define	libname	%mklibname %{name} %{api} %{major}
%define	devname	%mklibname -d %{name}

Summary:	A DBUS packaging abstraction layer
Name:		packagekit-qt
Version:	0.8.7
Release:	1
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0:	http://www.packagekit.org/releases/PackageKit-Qt-%{version}.tar.xz
URL:		http://www.packagekit.org
BuildRequires:	packagekit >= %{version}
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	cmake
Requires:	packagekit >= %{version}

%description
PackageKit is a DBUS abstraction layer that allows the session user to manage
packages in a secure way using a cross-distro, cross-architecture API.

%package -n	%{libname}
Summary:	Libraries for accessing PackageKit-Qt
Group:		System/Configuration/Packaging
Obsoletes:	%{_lib}packagekit-qt-qt2_5 < 0.8.6-2
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

%prep
%setup -q -n PackageKit-Qt-%{version}
%apply_patches

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/lib%{name}%{api}.so.%{major}
%{_libdir}/lib%{name}%{api}.so.%{version}

%files -n %{devname}
%{_includedir}/PackageKit/%{name}%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/%{name}%{api}
