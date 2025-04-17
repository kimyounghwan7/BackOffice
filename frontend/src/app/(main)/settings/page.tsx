'use client'
import { Fragment } from 'react'
import { Button } from '@/components/ui/button'

export default function ArchiveList() {
	return (
		<Fragment>
			<div className="flex w-full gap-2 px-4 justify-end">
				<Button className="max-w-[8rem] flex-1" variant={'default'}>
					settings
				</Button>
			</div>
		</Fragment>
	)
}
