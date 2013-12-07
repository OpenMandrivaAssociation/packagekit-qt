%define	api	2
%define	major	6
%define	libname	%mklibname %{name} %{api} %{major}
%define	devname	%mklibname -d %{name}

Summary:	A DBUS packaging abstraction layer
Name:		packagekit-qt
Version:	0.8.8
Release:	5
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://www.packagekit.org
Source0:	http://www.packagekit.org/releases/PackageKit-Qt-%{version}.tar.xz
Patch0:		PackageKit-Qt-0.8.7-fix-pkgconfig-libdir-path.patch
BuildRequires:	cmake
BuildRequires:	packagekit >= %{version}
BuildRequires:	pkgconfig(QtCore)
Requires:	packagekit >= %{version}

%description
PackageKit is a DBUS abstraction layer that allows the session user to manage
packages in a secure way using a cross-distro, cross-architecture API.

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

%prep
%setup -qn PackageKit-Qt-%{version}
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

