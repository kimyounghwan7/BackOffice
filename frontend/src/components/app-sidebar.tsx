import { Archive, Book, Megaphone, NotebookPen, Search, Settings, UsersRound } from 'lucide-react'

import {
	Sidebar,
	SidebarContent,
	SidebarHeader,
	SidebarMenu,
	SidebarMenuButton,
	SidebarMenuItem
} from '@/components/ui/sidebar'
import { AppSidebarGroup } from './app-sidebar-grop'

// Menu items.
// TODO 추후에 DB에 menu 관리하게 변경.
export const menuItems = [
	{
		title: 'Search',
		url: '/search',
		icon: Search
	},
	{
		title: 'Announcement',
		url: '/announcement',
		icon: Megaphone
	},
	{
		title: 'Archive',
		url: '/archive',
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
		url: '/users',
		icon: UsersRound
	},
	{
		title: 'Settings',
		url: '/settings',
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
				<AppSidebarGroup />
			</SidebarContent>
		</Sidebar>
	)
}
