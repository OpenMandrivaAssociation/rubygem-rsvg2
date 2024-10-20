%define rbname rsvg2

Summary:	Ruby binding of librsvg-2.x
Name:		rubygem-%{rbname}
Version:	2.2.0
Release:	2
License:	LGPLv2.1+
Group:		Development/Ruby
Url:		https://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygem-cairo-devel
BuildRequires:	rubygem-glib2-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(ruby)
BuildRequires:	rubygem(cairo)
BuildRequires:	rubygem(glib2)

%description
Ruby binding of librsvg-2.x.

%files
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/%{rbname}.so

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

