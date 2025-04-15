import { Archive, Book, Megaphone, NotebookPen, Search, Settings, UsersRound } from 'lucide-react'

import {
	Sidebar,
	SidebarContent,
	SidebarGroup,
	SidebarGroupContent,
	SidebarGroupLabel,
	SidebarHeader,
	SidebarMenu,
	SidebarMenuButton,
	SidebarMenuItem
} from '@/components/ui/sidebar'

// Menu items.
// TODO 추후에 DB에 menu 관리하게 변경.
export const menuItems = [
	{
		title: 'Search',
		url: '#',
		icon: Search
	},
	{
		title: 'Announcement',
		url: '#',
		icon: Megaphone
	},
	{
		title: 'Archive',
		url: '#',
		icon: Archive
	},
	{
		title: 'Report',
		url: '/report',
		icon: Book
	}
]

export const adminMenuItems = [
	{
		title: 'Users',
		url: '#',
		icon: UsersRound
	},
	{
		title: 'Settings',
		url: '#',
		icon: Settings
	}
]

export function AppSidebar() {
	return (
		<Sidebar variant="inset">
			<SidebarHeader>
				<SidebarMenu>
					<SidebarMenuItem>
						<SidebarMenuButton
							asChild
							className="data-[slot=sidebar-menu-button]:!p-1.5"
						>
							<a href="/">
								<NotebookPen className="h-5 w-5" />
								<span className="text-base font-semibold">Back Office.</span>
							</a>
						</SidebarMenuButton>
					</SidebarMenuItem>
				</SidebarMenu>
			</SidebarHeader>
			<SidebarContent>
				<SidebarGroup>
					<SidebarGroupLabel>Genral</SidebarGroupLabel>
					<SidebarGroupContent>
						<SidebarMenu>
							{menuItems.map(item => (
								<SidebarMenuItem key={item.title}>
									<SidebarMenuButton asChild>
										<a href={item.url}>
											<item.icon />
											<span>{item.title}</span>
										</a>
									</SidebarMenuButton>
								</SidebarMenuItem>
							))}
						</SidebarMenu>
					</SidebarGroupContent>
				</SidebarGroup>
				<SidebarGroup>
					<SidebarGroupLabel>Admin</SidebarGroupLabel>
					<SidebarGroupContent>
						<SidebarMenu>
							{adminMenuItems.map(item => (
								<SidebarMenuItem key={item.title}>
									<SidebarMenuButton asChild>
										<a href={item.url}>
											<item.icon />
											<span>{item.title}</span>
										</a>
									</SidebarMenuButton>
								</SidebarMenuItem>
							))}
						</SidebarMenu>
					</SidebarGroupContent>
				</SidebarGroup>
			</SidebarContent>
		</Sidebar>
	)
}
