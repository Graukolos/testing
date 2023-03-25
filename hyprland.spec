Name:           hyprland
Version:        0.23.0
Release:        %autorelease
Summary:        Hyprland is a dynamic tiling Wayland compositor based on wlroots that doesn't sacrifice on its looks.

License:        BSD-3-Clause
URL:            https://hyprland.org/
Source:         https://github.com/hyprwm/Hyprland/archive/refs/tags/v0.23.0beta.tar.gz        

BuildRequires:  xorg-x11-server-Xwayland-devel
Requires:       xorg-x11-server-Xwayland

%description


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Sat Mar 25 2023 Max Erdelmeier <graukolos@graukolos.tech>
- 
