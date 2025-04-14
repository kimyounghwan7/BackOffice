import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
	experimental: {
		optimizeCss: process.env.LIGHTNINGCSS !== 'false'
	}
}

export default nextConfig
