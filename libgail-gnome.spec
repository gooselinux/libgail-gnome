%define libgnomeui_version 2.0.1
%define gtk2_version 2.0.3
%define atk_version 1.0.2
%define at_spi_version 1.0.1
%define at_spi_release 2

Summary: Accessibility implementation for GTK+ and GNOME libraries
Name: libgail-gnome
Version: 1.20.1
Release: 4.1%{?dist}
URL: http://developer.gnome.org/projects/gap
Source0: http://download.gnome.org/sources/libgail-gnome/1.20/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

Requires: atk >= %{atk_version}
Requires: gtk2 >= %{gtk2_version}
Requires: libgnomeui >= %{libgnomeui_version}
Requires: at-spi >= %{at_spi_version}

BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: atk-devel >= %{atk_version}
BuildRequires: libgnomeui-devel >= %{libgnomeui_version}
BuildRequires: at-spi-devel >= %{at_spi_version}-%{at_spi_release}
BuildRequires: gnome-panel-devel

%description
GAIL implements the abstract interfaces found in ATK for GTK+ and GNOME 
libraries, enabling accessibility technologies such as at-spi to access 
those GUIs. 

libgail-gnome contains the GNOME portions of GAIL.

%package devel
Summary: Files to compile applications that use the GNOME portions of GAIL
Group: Development/Libraries
Requires: %name = %{version}

Requires: atk-devel
Requires: libbonoboui-devel
Requires: gtk2-devel
Requires: pkgconfig

%description devel
libgail-gnome-devel contains the files required to compile applications against 
the GNOME portions of the GAIL libraries.

%prep
%setup -q

%build

%configure

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

make ##%{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# Remove unpackaged files
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/modules/*

%files devel
%{_libdir}/pkgconfig/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.20.1-4.1
- Rebuilt for RHEL 6

* Mon Aug  3 2009 Matthias Clasen <mclasen@redhat.com> - 1.20.1-4
- Drop unneeded direct deps

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 1.20.1-1
- Update to 1.20.1

* Fri Feb  8 2008 Matthias Clasen <mclasen@redhat.com> - 1.20.0-2
- Rebuild for gcc 4.3

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 1.20.0-1
- Update to 1.20.0

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.19.5-2
- Rebuild for selinux ppc32 issue.

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 1.19.5-2
- Update license field

* Tue Jul 10 2007 Matthias Clasen <mclasen@redhat.com> - 1.19.5-1
- Update to 1.19.5

* Sat Jul  7 2007 Matthias Clasen <mclasen@redhat.com> - 1.18.0-3
- Fix directory ownership issues

* Thu Mar 15 2007 Karsten Hopp <karsten@redhat.com> 1.18.0-2
- rebuild with current gtk2 to add png support (#232013)

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 1.18.0-1
- Update to 1.18.0

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1.3-1.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.1.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.1.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com> 
- Update to 1.1.3

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 30 2005 Matthias Clasen <mclasen@redhat.com> 1.1.2-1
- Update to 1.1.2

* Wed Mar 30 2005 Matthias Clasen <mclasen@redhat.com> 1.1.0-4
- Split off a -devel package.  (#152499)

* Sun Mar  6 2005 Matthias Clasen <mclasen@redhat.com> 1.1.0-3
- Add a BuildRequires for gnome-panel-devel (#137544)
- Include the .pc file (#119742)

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> 1.1.0-2
- Rebuild with gcc4

* Thu Aug  5 2004 Mark McLoughlin <markmc@redhat.com> 1.1.0-1
- Update to 1.1.0

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jul 30 2003 Havoc Pennington <hp@redhat.com> 1.0.2-2
- rebuild

* Wed Jul  9 2003 Havoc Pennington <hp@redhat.com> 1.0.2-1
- 1.0.2
- no longer need to fix location of gtk modules

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 11 2003 Havoc Pennington <hp@redhat.com> 1.0.0-6
- rebuild with new at-spi

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec 13 2002 Tim Powers <timp@redhat.com> 1.0.0-4
- remove unpackaged files from the buildroot

* Mon Jun 24 2002 Matt Wilson <msw@redhat.com>
- modules go in gtk-2.0/modules, not gtk-2.0

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Havoc Pennington <hp@redhat.com>
- initial package

