%define		file_version	%(echo %{version} | tr . -)
Summary:	Sega Master System Emulator
Summary(pl.UTF-8):	Emulator Sega Master System
Name:		osmose
Version:	0.9.96
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://bcz.asterope.fr/osmose/Osmose-%{file_version}-QT.zip
# Source0-md5:	256b393d83270620e98f39e0cfb11359
Patch0:		%{name}-Makefile.patch
URL:		http://bcz.asterope.fr/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Osmose is an Object oriented sega master system designed for first for
Linux.

%description -l pl.UTF-8
Osmose jest obiektowo zorientowanym systemem sega master stworzonym
przede wszystkim dla Linuksa.

%prep
%setup -q -n Osmose-%{file_version}-QT

%undos Makefile
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install Osmose-0-9-96-QT $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.txt TODO.txt
%attr(755,root,root) %{_bindir}/osmose
