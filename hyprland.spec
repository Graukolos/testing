Name:           hyprland
Version:        v0.23.0beta
Release:        %autorelease
Summary:        Hyprland is a dynamic tiling Wayland compositor based on wlroots that doesn't sacrifice on its looks.

License:        BSD-3-Clause
URL:            https://hyprland.org/
Source:         https://github.com/hyprwm/Hyprland/releases/download/v0.23.0beta/source-%{version}.tar.gz        
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  jq
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  glslang

%description


%prep
%autosetup -n %{name}-source


%build
%meson -DLEGACY_RENDERER:BOOL=true -Dwlroots:xcb-errors=disabled
%meson_build

%install
%meson_install


%files
%{_bindir}/Hyprland
%{_bindir}/hyprctl
%{_mandir}/man1/hyprctl.1.gz
%{_mandir}/man1/Hyprland.1.gz
%{_datadir}/hyprland
%{_datadir}/wayland-sessions/hyprland.desktop

%changelog
* Sat Mar 25 2023 Max Erdelmeier <graukolos@graukolos.tech>
- 
