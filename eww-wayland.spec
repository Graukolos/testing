Name:           eww-wayland
Version:        0.4.0
Release:        %{autorelease}
Summary:        ELKowars wacky widgets

License:        MIT
URL:            https://github.com/elkowar/eww
Source:         https://github.com/elkowar/eww/archive/refs/tags/eww-%{version}.tar.gz

BuildRequires:  gcc

%global debug_package %{nil}

%description
Elkowars Wacky Widgets is a standalone widget system made in Rust that allows you to implement your own, custom widgets in any window manager.

%prep
%autosetup -n eww-%{version}
export RUSTUP_HOME=%{_builddir}/.rustup
export CARGO_HOME=%{_builddir}/.cargo
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain nightly -y
export PATH=%{_builddir}/.cargo/bin:$PATH

%build
export RUSTUP_HOME=%{_builddir}/.rustup
export CARGO_HOME=%{_builddir}/.cargo
export PATH=%{_builddir}/.cargo/bin:$PATH
cargo build --release --no-default-features --features=wayland

%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -m 755 %{_builddir}/eww-%{version}/target/release/eww %{buildroot}%{_bindir}/eww

%files
%{_bindir}/eww
