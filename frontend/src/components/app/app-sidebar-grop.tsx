import { Fragment } from 'react'
import {
	SidebarGroup,
	SidebarGroupContent,
	SidebarGroupLabel,
	SidebarMenu,
	SidebarMenuButton,
	SidebarMenuItem
} from '@/components/ui/sidebar'
import { Archive, Book, Megaphone, Search, Settings, UsersRound } from 'lucide-react'
import {
	ROUTER_ANNOUNCEMENT,
	ROUTER_ARCHIVE,
	ROUTER_REPORT,
	ROUTER_SEARCH,
	ROUTER_SETTINGS,
	ROUTER_USERS
} from '@/constants/routers'

// Menu items.
// TODO 추후에 DB에 menu 관리하게 변경.
const appMenuItems = [
	{
		group: 'General',
		items: [
			{
				title: 'Search',
				url: ROUTER_SEARCH,
				icon: Search
			},
			{
				title: 'Announcement',
				url: ROUTER_ANNOUNCEMENT,
				icon: Megaphone
			},
			{
				title: 'Archive',
				url: ROUTER_ARCHIVE,
				icon: Archive
			},
			{
				title: 'Report',
				url: ROUTER_REPORT,
				icon: Book
			}
		]
	},
	{
		group: 'Admin',
		items: [
			{
				title: 'Users',
				url: ROUTER_USERS,
				icon: UsersRound
			},
			{
				title: 'Settings',
				url: ROUTER_SETTINGS,
				icon: Settings
			}
		]
	}
]

export function AppSidebarGroup() {
	return (
		<Fragment>
			{appMenuItems.map(group => (
				<SidebarGroup key={group?.group}>
					<SidebarGroupLabel>{group?.group}</SidebarGroupLabel>
					<SidebarGroupContent>
						<SidebarMenu>
							{group?.items?.map(item => (
								<SidebarMenuItem key={item?.title}>
									<SidebarMenuButton asChild>
										<a
											href={item?.url ?? ''}
											className="flex items-center gap-2"
										>
											<item.icon className="w-4 h-4" />
											<span>{item?.title ?? ''}</span>
										</a>
									</SidebarMenuButton>
								</SidebarMenuItem>
							))}
						</SidebarMenu>
					</SidebarGroupContent>
				</SidebarGroup>
			))}
		</Fragment>
	)
}
