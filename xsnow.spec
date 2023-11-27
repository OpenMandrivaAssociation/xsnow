Name:           xsnow
Version:        3.7.6
Release:        1
Summary:        Let it snow on your desktop
 
License:        GPLv3+
URL:            https://sourceforge.net/projects/xsnow/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         snow-bindir.patch

BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  desktop-file-utils
BuildRequires:  appstream-util
 
 
%description
Xsnow is a X Window application that will snow on the desktop background.
Santa and his reindeer will complete your festive-season feeling.
Xsnow runs in GNOME, KDE, FVWM and desktops that are derived from those.
 
%prep
%autosetup -p1

# Fix Makefile
#sed -i 's!$(exec_prefix)/games!$(exec_prefix)/bin!' src/Makefile.in
 
%build
%configure --disable-selfrep
%make_build
 
%install
%make_install
# Fix icon path
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mv %{buildroot}%{_datadir}/pixmaps/%{name}.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
 
# Validate desktop file
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
 
# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%find_lang %{name}
 
%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6*
%{_metainfodir}/%{name}.appdata.xml
%license COPYING
%doc AUTHORS README.md
